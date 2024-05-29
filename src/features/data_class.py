from datetime import datetime

# Define the date format to be used
time_format = '%Y-%m-%d'


class DataClass:
    """
    Class for handling date-related data operations.

    Attributes:
        data (any): The data to be handled.
        start_date (datetime.date): The start date for data operations.
        end_date (datetime.date): The end date for data operations.

    Methods:
        update_data(new_data): Updates the data attribute with new data.
    """

    def __init__(self, start_date: str, end_date: str):
        """
        Initialize the DataClass with start and end dates.

        Args:
            start_date (str): The start date in string format.
            end_date (str): The end date in string format.
        """
        self.data = None  # Initialize data attribute to None
        self.start_date = datetime.strptime(start_date, time_format).date()  # Convert start date string to date object
        self.end_date = datetime.strptime(end_date, time_format).date()  # Convert end date string to date object

    def update_data(self, new_data):
        """
        Update the data attribute with new data.

        Args:
            new_data (any): The new data to be updated.
        """
        self.data = new_data  # Assign new data to data attribute


if __name__ == "__main__":
    pass
