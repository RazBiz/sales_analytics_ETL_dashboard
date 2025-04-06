from prefect import flow, task
from etl.extract import extract_sales_data, extract_store_metadata
from etl.transform import clean_sales_data, merge_data
from etl.load import load_to_postgres

@task
def run_etl():
    sales_df = extract_sales_data('data/sales.csv')
    store_df = extract_store_metadata('data/stores.csv')
    cleaned = clean_sales_data(sales_df)
    merged = merge_data(cleaned, store_df)
    load_to_postgres(merged, 'sales', 'postgresql://postgres:password@localhost:5432/retaildb')

@flow
def etl_flow():
    run_etl()

if __name__ == '__main__':
    etl_flow()