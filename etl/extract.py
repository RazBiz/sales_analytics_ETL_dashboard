import pandas as pd

def extract_sales_data(csv_path):
    return pd.read_csv(csv_path)

def extract_store_metadata(stores_csv_path):
    return pd.read_csv(stores_csv_path)
