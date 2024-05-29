try:
    from abc import ABC, abstractmethod  # Module for defining abstract base classes
    # print('Modules imported successfully.')
except ImportError as import_error:
    print(import_error)


class BaseDBClass(ABC):
    """
    Abstract base class for database connections.

    Attributes:
        config: Dictionary containing database configuration parameters.
        cursor: Database cursor object.
    """

    def __init__(self, config):
        """
        Constructor method for BaseDBClass.

        Args:
            config (dict): Dictionary containing database configuration parameters.
        """
        self.config = config
        self.cursor = None

    @abstractmethod
    def connect(self):
        """
        Abstract method to establish a database connection.
        """
        pass

    @abstractmethod
    def load_data(self, data):
        """
        Abstract method to load data into the database.

        Args:
            data: Data to be loaded into the database.
        """
        pass

    @abstractmethod
    def close(self):
        """
        Abstract method to close the database connection.
        """
        pass
