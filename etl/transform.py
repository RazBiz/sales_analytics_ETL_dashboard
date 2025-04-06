import pandas as pd

def clean_sales_data(df):
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    df['total_price'] = df['quantity'] * df['unit_price']
    return df

def merge_data(sales_df, store_df):
    return sales_df.merge(store_df, on='store_id', how='left')
