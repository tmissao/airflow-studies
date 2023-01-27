from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

DEFAULT_ARGS = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 20),
    'email': 'owner@test.com',
    'retries': 3,
    'retry_delay': timedelta(seconds=30),
}

with DAG(
    dag_id="backfill",
    schedule="0 0 * * *", # same result
    default_args=DEFAULT_ARGS,
    # Performs a schedule catchup (calculates how many executions was lose between startdate and current date and execute them)
    catchup=True,
) as dag:

    task_1 = BashOperator(task_id='task_1', bash_command="echo 'first task'")
    
    task_2 = BashOperator(task_id='task_2', bash_command="echo 'second task'")

    task_1 >> task_2