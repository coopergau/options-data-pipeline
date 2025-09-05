from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess
import sys

def run_options_collector():
    result = subprocess.run([sys.executable, '/opt/airflow/src/main.py'], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")
    print(f"Output: {result.stdout}")

with DAG(
    dag_id="options_data_collector",
    start_date=datetime(2025, 9, 1),
    schedule_interval="0 9 * * 1-5",
    catchup=False,
) as dag:
    
    collect_options_data = PythonOperator(
        task_id="collect_options_data",
        python_callable=run_options_collector
    )