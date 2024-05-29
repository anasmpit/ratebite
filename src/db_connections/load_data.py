from features.data_class import DataClass
from db_connections.postgres_db import PostgresDBClass
from config.db_config import DATABASE_CONFIG


class LoadDataClass:
    """
    Class for loading data into the database.

    Attributes:
        data_class_instance (DataClass): Instance of DataClass containing data to be loaded.
        db_type (str): Type of the database (e.g., 'postgres').
    """

    def __init__(self, data_class_instance: DataClass, db_type: str):
        """
        Constructor method for LoadDataClass.

        Args:
            data_class_instance (DataClass): Instance of DataClass containing data to be loaded.
            db_type (str): Type of the database.
        """
        self.data_class_instance = data_class_instance
        self.db_type = db_type

    def get_db_connection(self) -> PostgresDBClass:
        """
        Method to get a database connection based on the database type.

        Returns:
            PostgresDBClass: Database connection object.
        """
        if self.db_type == 'postgres':
            return PostgresDBClass(DATABASE_CONFIG['postgres'])
        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")

    def load_data_to_database(self) -> None:
        """
        Method to load data into the database.
        """
        # Establish the connection with the Database
        db_connection = self.get_db_connection()
        db_connection.connect()
        db_connection.load_data(self.data_class_instance.data)
        db_connection.export_materialized_view()
        db_connection.export_today_view()
        db_connection.print_materialized_view()
        db_connection.cursor_close()
        db_connection.close()
