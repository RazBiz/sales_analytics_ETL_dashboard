import pandas as pd

def extract_sales_data(sales_csv_path):
    """
        Extracts sales data from a CSV file.

        This function reads a CSV file containing sales data and returns it as a Pandas DataFrame.
        It can be modified to extract data from other sources like an API if needed.

        :param sales_csv_path: The file path to the CSV containing sales data.
        :return: A Pandas DataFrame containing the sales data from the CSV file.
        """
    return pd.read_csv(sales_csv_path)

def extract_store_metadata(stores_csv_path):
    """
    Extracts store metadata from a CSV file.

    This function reads a CSV file containing store data and returns it as a Pandas DataFrame.
    It can be modified to extract data from other sources like an API if needed.

    :param stores_csv_path: The file path to the CSV containing store metadata.
    :return: A Pandas DataFrame containing the store metadata from the CSV file.
    """
    return pd.read_csv(stores_csv_path)
