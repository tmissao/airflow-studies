import pendulum
from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'start_date': datetime(2023, 1, 26),
    'owner': 'Airflow',
    'email': 'owner@test.com',
    'retries': 3,
    'retry_delay': timedelta(seconds=30),
}

def second_task():
    print('Hello from second_task')
    # raise ValueError('This will turns the python task in failed state')

def third_task():
    print('Hello from third_task')
    # raise ValueError('This will turns the python task in failed state')

with DAG(
  dag_id='depends_task', 
  schedule_interval="*/1 * * * *", 
  default_args=default_args,
  catchup=False
) as dag:
    
    # Task 1
    bash_task_1 = BashOperator(task_id='bash_task_1', bash_command="echo 'first task'")
    
    # Task 2
    python_task_2 = PythonOperator(task_id='python_task_2', python_callable=second_task, depends_on_past=True)

    # Task 3
    python_task_3 = PythonOperator(task_id='python_task_3', python_callable=third_task)

    bash_task_1 >> python_task_2 >> python_task_3