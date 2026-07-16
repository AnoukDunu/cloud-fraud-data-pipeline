from google.cloud import bigquery

client = bigquery.Client()

def load(df):
    table_id = "cloud-fraud-detection-pipeline.transactions_dataset.transactions"
    job = client.load_table_from_dataset(df, table_id)
    job.result()