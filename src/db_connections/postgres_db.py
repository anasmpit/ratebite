try:
    import psycopg2
    import typing
    import pandas as pd
    import datetime

    from tabulate import tabulate
    from db_connections.base_db import BaseDBClass

    # print('Modules imported successfully.')
except ImportError as import_error:
    print(import_error)

"""
    Key note:
    
    Of course, SQLAlchemy can be used for easier manipulation of various RDBMS.
    Here, we demonstrate a solution based clearly on OOP. 
"""
time_format = '%Y-%m-%d'


class PostgresDBClass(BaseDBClass):
    """
    Class for interacting with a PostgreSQL database.

    Inherits from BaseDBClass.

    Methods:
        connect(): Establish a connection with the database.
        load_data(data: pd.DataFrame): Load data into the database.
        export_materialized_view(): Export materialized view.
        print_materialized_view(): Print materialized view.
        export_today_view(): Export today's view.
        close(): Close the connection with the database.
        cursor_close(): Close the cursor.
    """

    def connect(self):
        """
        Establish a connection with the PostgreSQL database.
        """
        try:
            # Establish a connection to the PostgreSQL database using provided config
            self.connection = psycopg2.connect(
                dbname=self.config['dbname'],
                user=self.config['user'],
                password=self.config['password'],
                host=self.config['host'],
                port=self.config['port']
            )

            # Disable autocommit for bulk loading, commit changes at the end
            self.connection.autocommit = False

            print("Connections established.")
        except psycopg2.Error as error:
            print(f"Unable to connect to the database: {error}")
            exit()

    def load_data(self, data: pd.DataFrame) -> None:
        """
        Load data into the PostgreSQL database.

        Args:
            data (pd.DataFrame): DataFrame containing the data to be loaded.
        """
        print("Loading data by connector.\n")
        self.cursor = self.connection.cursor()

        try:
            # Create Postgres schema if it doesn't exist
            create_schema_query = "CREATE SCHEMA IF NOT EXISTS import ;"
            self.cursor.execute(create_schema_query)

            # Create exchange rates table if it doesn't exist
            create_table_query = """
                    CREATE TABLE IF NOT EXISTS "import".exchange_rates_table (
                        id SERIAL,
                        currency_date date NOT NULL,
                        currency_symbol varchar NOT NULL,
                        currency_rate float4 NOT NULL,
                        UNIQUE(currency_date, currency_symbol)
                        );"""
            self.cursor.execute(create_table_query)

            # Query to fetch existing dates from the database
            existing_dates_query = """SELECT DISTINCT currency_date FROM "import".exchange_rates_table;"""

            # Execute the query to retrieve existing dates
            self.cursor.execute(existing_dates_query)
            existing_dates_result = self.cursor.fetchall()

            # Extract the dates from the result
            existing_dates = [date[0].strftime(time_format) for date in existing_dates_result]

            # Load data from pandas DataFrames

            # Data will be manipulated as solid tuples and NOT via SQLAlchemy
            # Convert DataFrame to a list of solid tuples for raw SQL
            # which is faster, avoiding the overhead of the ORM layer
            tuples = [tuple(x) for x in data.to_numpy()]

            # SQL Insert Statement
            # Make sure that any importing dates  on conflict with already
            # existing do replace the old ones
            insert_query = """INSERT INTO "import".exchange_rates_table
                                (currency_date, currency_symbol, currency_rate)
                                VALUES (%s, %s, %s)
                                ON CONFLICT (currency_date, currency_symbol)
                                DO UPDATE SET
                                    currency_rate = EXCLUDED.currency_rate
                                RETURNING currency_date
                                ;"""

            self.cursor.executemany(insert_query, tuples)

            # Query to fetch updated dates from the database
            updated_dates_query = """SELECT DISTINCT currency_date FROM "import".exchange_rates_table;"""

            # Execute the query to retrieve updated dates
            self.cursor.execute(updated_dates_query)
            updated_dates_result = self.cursor.fetchall()

            # Extract the dates from the result
            updated_dates = [date[0].strftime(time_format) for date in updated_dates_result]

            common_dates = set(existing_dates).intersection(set(updated_dates))
            if common_dates:
                print(f"Overwriting existing records for dates: {common_dates}.\n"
                      f"The above are being replaced by the new ones.\n")

            self.connection.commit()
        except psycopg2.Error as error:
            print(f"Error executing query: {error}")
            self.connection.rollback()

    def export_materialized_view(self):
        """
        Export a materialized view of the data.
        """
        try:
            self.cursor = self.connection.cursor()

            # Create materialized rates table if it doesn't exist
            materialized_view_query = """
                       CREATE MATERIALIZED VIEW IF NOT EXISTS "import".monthly_stats AS
                            SELECT
                                MIN(currency_rate) AS min_rate,
                                MAX(currency_rate) AS max_rate,
                                AVG(currency_rate) AS avg_rate,
                                EXTRACT(MONTH FROM currency_date) AS month,
                                EXTRACT(YEAR FROM currency_date) AS year
                            FROM
                                "import".exchange_rates_table
                            GROUP BY
                                EXTRACT(MONTH FROM currency_date),
                                EXTRACT(YEAR FROM currency_date)
                        ;"""
            self.cursor.execute(materialized_view_query)

            # Refresh the materialized view
            refresh_materialized_view_query = """
                            REFRESH MATERIALIZED VIEW "import".monthly_stats;
                        """
            self.cursor.execute(refresh_materialized_view_query)

            self.connection.commit()
        except psycopg2.Error as error:
            print(f"Error executing query: {error}")
            self.connection.rollback()

    def print_materialized_view(self):
        """
        Print the materialized view in a tabular format.
        """
        try:
            # Query to fetch the materialized view from the database
            materialized_view_select_query = """
                                    SELECT *,
                                        TO_DATE(CONCAT(year, '-', month, '-01'), 'YYYY-MM-DD') AS full_date
                                    FROM "import".monthly_stats
                                    ORDER BY full_date ASC
                                    ;"""
            self.cursor.execute(materialized_view_select_query)

            # Extract all rows from the materialized view table
            materialized_view_results = self.cursor.fetchall()

            # Define headers for the tabulate table
            headers = ["Min Rate", "Max Rate", "Avg Rate", "Month/Year"]

            # Define a list to store all rows
            rows = []

            # Loop through each row in the result and format the month/year
            for row in materialized_view_results:
                max_rate, min_rate, avg_rate, month, year = row[:-1]

                # Get the month name
                month_name = [
                    'January', 'February', 'March', 'April',
                    'May', 'June', 'July', 'August',
                    'September', 'October', 'November', 'December'
                ][int(month) - 1]

                # Append the formatted row to the list of rows
                rows.append([min_rate, max_rate, avg_rate, f"{month_name} {int(year)}"])

            # Print the table using tabulate
            print("---- Some rate statistics per month.")
            print(tabulate(rows, headers=headers, tablefmt="psql"), end="\n\n")
        except psycopg2.Error as error:
            print(f"Error executing query: {error}")
            self.connection.rollback()

    def export_today_view(self):
        """
        Export a view of today's rates.
        """
        try:
            self.cursor = self.connection.cursor()

            # Create a view for today's rates
            today_view_query = """
                       CREATE OR REPLACE VIEW "import".today_rates_view AS
                            SELECT *
                            FROM "import".exchange_rates_table
                            WHERE currency_date = CURRENT_DATE;
                        ;"""
            self.cursor.execute(today_view_query)

            # Query to fetch today's rates from the view
            today_view_select_query = """
                           SELECT *
                           FROM "import".today_rates_view
                           ;"""
            self.cursor.execute(today_view_select_query)

            # Extract all rows from the view
            today_view_results = self.cursor.fetchall()

            # Define headers for the tabulate table
            headers = ["Currency date", "Currency symbol", "Currency rate"]

            # Define a list to store all rows
            rows = []

            # Loop through each row in the result and format the data
            for row in today_view_results:
                currency_date, currency_symbol, currency_rate = row[1:]

                # Append the formatted row to the list of rows
                rows.append([currency_date, currency_symbol, currency_rate])

            # Print the table using tabulate
            print("---- Today's rates.")
            print(tabulate(rows, headers=headers, tablefmt="psql"), end="\n\n")

            self.connection.commit()
        except psycopg2.Error as error:
            print(f"Error executing query: {error}")
            self.connection.rollback()

    def close(self):
        """
        Close the connection to the PostgreSQL database.
        """
        print(f"Connection closed.")
        self.connection.close()

    def cursor_close(self):
        """
        Close the cursor.
        """
        print("Cursor closed.")
        self.cursor.close()
