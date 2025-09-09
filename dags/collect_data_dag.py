from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.collect_data import collect_options_data

with DAG(
    dag_id='options_data_collector',
    description='Pulls option chain data and saves it to PostgreSQL tables in RDS',
    start_date=datetime(2025, 9, 1),
    schedule_interval='0 9 * * 1-5',
    catchup=False,
) as dag:
    
    collect_options_data = PythonOperator(
        task_id='collect_options_data',
        python_callable=collect_options_data
    )