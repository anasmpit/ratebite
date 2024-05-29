try:
    # using requests over http module, because
    #     https: // stackoverflow.com / questions / 39435443 / why - is -python - 3 -
    #     http - client - so - much - faster - than - python - requests
    import requests
    import sys
    import json
    from typing import Dict
    from datetime import datetime, timedelta

    from features.data_class import DataClass
    # print('Modules imported successfully.')
except ImportError as import_error:
    print(import_error)

# TODO: Make sure to set the below params as args to the CLI
API_KEY = 'your_API_key'  # API key for accessing the exchange rates API
time_format = '%Y-%m-%d'  # Date format string


class FetchingDataClass:
    """
    Class for fetching exchange rate data.

    Attributes:
        data_class_instance (DataClass): An instance of DataClass containing date range and data.
        url (str): URL for the API request.
        headers (dict): Headers for the API request.
        params (dict): Parameters for the API request.

    Methods:
        configure_api_params(): Configures the API parameters.
        get_exchange_rate(specific_date): Fetches exchange rate data for a specific date.
        get_exchange_rates_for_period(): Fetches exchange rate data for a date range.
        fetch_data(): Fetches and updates the data in the DataClass instance.
    """

    def __init__(self, data_class_instance: DataClass):
        """
        Initialize the FetchingDataClass with a DataClass instance.

        Args:
            data_class_instance (DataClass): An instance of DataClass.
        """
        self.data_class_instance = data_class_instance
        self.url = None
        self.headers = {"accept": "application/json"}  # Headers for the API request
        self.params = {"app_id": API_KEY}  # Parameters for the API request

    def configure_api_params(self):
        """
        Configure API parameters.
        """
        try:
            pass  # Configuration logic for the API parameters
        except Exception as error:
            print(error)

    def get_exchange_rate(self, specific_date: str) -> None:
        """
        Fetch exchange rate data for a specific date.

        Args:
            specific_date (str): The date for which to fetch exchange rates.

        Returns:
            dict: The exchange rate data in JSON format, or None if the request fails.

        Note: if specific_date reaches current date, then the request gets response for
            latest.json and not historical/{date}.json

        From source website https://docs.openexchangerates.org/reference/historical-json:

        Historical rates are generally the last values we published on a given UTC day
        (up to and including 23:59:59 UTC), with the exception of the current UTC date.

        If you make a request for the current day's historical file, you will receive
        the most recent rates available for your subscription plan at that moment, as
        the day is not yet complete (therefore in such cases, the values returned would
        be the same as you would find via our latest.json endpoint).

        If you wish to obtain rates for a historical date that is the same as today's
        date (in UTC), you may prefer to make use of the latest.json endpoint instead,
        in order to prevent unexpected behaviour.
        """
        try:
            if datetime.strptime(specific_date, time_format).date() == datetime.now().date():
                print(f"Fetching data for {specific_date} from latest.json.")
                self.url = f"https://openexchangerates.org/api/latest.json"
            else:
                print(f"Fetching data for {specific_date} from historical.json.")
                self.url = f"https://openexchangerates.org/api/historical/{specific_date}.json"

            response = requests.get(self.url, headers=self.headers, params=self.params)
            return response.json() if (response.status_code == 200) else None
        except Exception as error:
            print(error)

    def get_exchange_rates_for_period(self) -> Dict[any, any]:
        """
        Fetch exchange rate data for a date range.

        Returns:
            dict: A dictionary with dates as keys and exchange rate data as values.
        """
        date_range = []
        current_date = self.data_class_instance.start_date

        if self.data_class_instance.end_date:
            while current_date <= self.data_class_instance.end_date:
                date_range.append(current_date.strftime(time_format))
                current_date += timedelta(days=1)

        exchange_rates = {}

        for date in date_range:
            data = self.get_exchange_rate(date)
            if data:
                exchange_rates[date] = data
        return exchange_rates

    def fetch_data(self) -> None:
        """
        Fetch and update the data in the DataClass instance.
        """
        fetched_data = self.get_exchange_rates_for_period()
        self.data_class_instance.update_data(fetched_data)
