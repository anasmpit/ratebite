try:
    import sys
    import json
    import pandas as pd
    from typing import Any, List, Dict

    from features.data_class import DataClass
    # print('Modules imported successfully.')
except Exception as import_error:
    print(import_error)


class TransformDataClass:
    """
    Class for transforming exchange rate data.

    Attributes:
        data_class_instance (DataClass): An instance of DataClass containing date range and data.
        base (str): Base currency for exchange rates.
        target (str): Target currency for exchange rates.
        db_type (str): Database type.

    Methods:
        create_dataframe(exchange_date): Creates a DataFrame from exchange rate data for a specific date.
        transform_data(): Transforms the exchange rate data into the desired format and updates DataClass instance.
    """

    def __init__(self, data_class_instance: DataClass):
        """
        Initialize the TransformDataClass with a DataClass instance.

        Args:
            data_class_instance (DataClass): An instance of DataClass.
        """
        self.data_class_instance = data_class_instance
        self.base = 'USD'  # Base currency
        self.target = 'EUR'  # Target currency
        self.db_type = 'postgres'  # Database type

        print(f"Exchange rates for {self.base} to {self.target}, for each date.", end='\n\n')
        # print(self.exchange_rates.keys())

    def create_dataframe(self, exchange_date: str) -> pd.DataFrame:
        """
        Create a DataFrame from exchange rate data for a specific date.

        Args:
            exchange_date (str): The date for which to create the DataFrame.

        Returns:
            pd.DataFrame: DataFrame containing the exchange rate data.
        """
        try:
            # Prepare the data dictionary for the DataFrame
            # print(f"Importing to pandas DataFrame for date -> {exchange_date}.")
            data = {
                "currency_date": exchange_date,
                "rate": self.data_class_instance.data[exchange_date]["rates"],
            }
            # Convert the dictionary to a DataFrame
            exchange_df = pd.DataFrame.from_dict(data)
            exchange_df = exchange_df.rename_axis("currency_symbol").reset_index()

            # Find the EUR rate and calculate the exchange rate for each currency
            eur_index = exchange_df.loc[exchange_df["currency_symbol"] == self.target].index[0]
            eur_rate = exchange_df.at[eur_index, "rate"]

            # print(f"Building equation for US: {us_rate} -> EUR: {eur_rate}.", end="\n\n")
            exchange_df = exchange_df.assign(currency_rate=lambda x: eur_rate / x["rate"])
            return exchange_df
        except Exception as error:
            print(error)

    def transform_data(self) -> None:
        """
        Transform the exchange rate data into the desired format and update the DataClass instance.
        """
        final_exchange_df = pd.DataFrame()

        # Iterate over each date and create a DataFrame, then concatenate them
        for exchange_date in self.data_class_instance.data:
            result = self.create_dataframe(exchange_date)
            final_exchange_df = pd.concat([final_exchange_df, result], axis=0)

        # Reset index and drop unnecessary columns
        final_exchange_df = final_exchange_df.reset_index().drop(["index", "rate"], axis=1)
        final_exchange_df = final_exchange_df[["currency_date", "currency_symbol", "currency_rate"]]

        # Update the data in the DataClass instance
        self.data_class_instance.update_data(final_exchange_df)
