try:
    from db_connections.base_db import BaseDBClass
except ImportError as import_error:
    print(import_error)


class MariaDBClass(BaseDBClass):
    """
    Class for interacting with a MariaDB database.

    Inherits from BaseDBClass.

    Methods:
        connect(): Establish a connection with the database.
        load_data(): Load data into the database.
        export_materialized_view(): Export materialized view.
        print_materialized_view(): Print materialized view.
        export_today_view(): Export today's view.
        close(): Close the connection with the database.
        cursor_close(): Close the cursor.
    """

    def connect(self):
        """
        Establish a connection with the database.
        """
        ...

    def load_data(self) -> None:
        """
        Load data into the database.
        """
        ...

    def export_materialized_view(self):
        """
        Export materialized view.
        """
        ...

    def print_materialized_view(self):
        """
        Print materialized view.
        """
        ...

    def export_today_view(self):
        """
        Export today's view.
        """
        ...

    def close(self):
        """
        Close the connection with the database.
        """
        ...

    def cursor_close(self):
        """
        Close the cursor.
        """
        ...
