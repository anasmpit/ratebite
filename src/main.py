import sys

from features.data_class import DataClass
from features.fetch_data_class import FetchingDataClass
from features.transform_data_class import TransformDataClass
from db_connections.load_data import LoadDataClass

from db_connections.postgres_db import PostgresDBClass
from config.db_config import DATABASE_CONFIG

def get_db_connection(db_type: str) -> PostgresDBClass:
    """
    Get a database connection based on the database type.

    Args:
        db_type (str): Type of database ('postgres' or other).

    Returns:
        PostgresDBClass: Instance of PostgresDBClass.

    Raises:
        ValueError: If the database type is not supported.
    """
    if db_type == 'postgres':
        return PostgresDBClass(DATABASE_CONFIG['postgres'])
    else:
        raise ValueError(f"Unsupported database type: {db_type}")


def main(start_date: str, end_date: str) -> None:
    """
    Main function for executing the data loading process.

    Args:
        start_date (str): Start date for fetching data.
        end_date (str): End date for fetching data.

    Returns:
        None
    """
    # Create an instance of DataClass with the provided start and end dates
    data_instance = DataClass(start_date, end_date)

    # Instantiate FetchingDataClass with the data_instance
    fetcher = FetchingDataClass(data_instance)
    fetcher.fetch_data()  # Fetch data using the fetcher instance

    # Instantiate TransformDataClass with the data_instance
    transformer = TransformDataClass(data_instance)
    transformer.transform_data()  # Transform the fetched data

    # Define the type of database (e.g., 'postgres')
    # TODO: this can be argument in CLI
    db_type = 'postgres'

    # Instantiate LoadDataClass with the data_instance and db_type
    loader = LoadDataClass(data_instance, db_type)
    loader.load_data_to_database()  # Load transformed data into the database


# Entry point of the script
if __name__ == "__main__":
    # Check if command-line arguments are provided
    if len(sys.argv) >= 2:
        start_date = sys.argv[1]  # Extract start date from the command-line argument
        # Extract end date from the command-line argument if provided, otherwise use start_date
        end_date = sys.argv[2] if len(sys.argv) > 2 else start_date

        # Call the main function with the provided start and end dates
        main(start_date, end_date)
    else:
        print("No valid dates(s) provided.")  # Print error message if no dates are provided
        sys.exit(1)  # Exit the script with a non-zero status code to indicate failure
