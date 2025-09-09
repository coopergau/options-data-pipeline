from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pytz
from src.collect_data import collect_options_data

with DAG(
    dag_id='options_data_collector',
    description='Pulls option chain data and saves it to PostgreSQL tables in RDS. Runs every hour from 9:30am to 4:30pm EST Mon-Fri. ' \
    'The 4:30 run is frozen at the data of market close (4:00pm)',
    start_date=datetime(2025, 9, 1, tzinfo=pytz.timezone('US/Eastern')),
    schedule_interval='30 9-16 * * 1-5',
    catchup=False,
) as dag:
    
    collect_options_data = PythonOperator(
        task_id='collect_options_data',
        python_callable=collect_options_data
    )