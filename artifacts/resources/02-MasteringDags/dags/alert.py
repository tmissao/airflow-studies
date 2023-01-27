from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

def on_success_dag(dict):
    print("on_success_dag")
    print(dict)


def on_failure_dag(dict):
    print("on_failure_dag")
    print(dict)

def on_success_task(dict):
    print("on_success_task")
    print(dict)


def on_failure_task(dict):
    print("on_failure_task")
    print(dict)

default_args = {
    'start_date': datetime(2023, 1, 26),
    'owner': 'Airflow',
    'retries': 3,
    'retry_delay': timedelta(seconds=30),
    'email': 'owner@test.com',
    'email_on_failure': True,
    'email_on_retry': False,
    'on_failure_callback': on_failure_task,
    'on_success_callback': on_success_task,
    'on_execution_timeout': timedelta(seconds=60)
}

with DAG(
    dag_id='alert_dag', 
    schedule_interval="0 0 * * *", 
    default_args=default_args, 
    catchup=True,
    dagrun_timeout=timedelta(minutes=3),
    on_success_callback=on_success_dag,
    on_failure_callback=on_failure_dag,
) as dag:
    
    # Task 1
    t1 = BashOperator(task_id='t1', bash_command="exit 1")
    
    # Task 2
    t2 = BashOperator(task_id='t2', bash_command="echo 'second task'")

    t1 >> t2