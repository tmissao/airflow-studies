from queue import Queue
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2023, 2, 1),
    'owner': 'Airflow',
    'email': 'owner@test.com'
}

with DAG(dag_id='queue_dag', schedule_interval='0 0 * * *', default_args=default_args, catchup=True) as dag:
    
    t_1_ssd = BashOperator(task_id='t_1_ssd', bash_command='echo "I/O intensive task"', queue="ssd")

    t_2_ssd = BashOperator(task_id='t_2_ssd', bash_command='echo "I/O intensive task"', queue="ssd")

    t_3_ssd = BashOperator(task_id='t_3_ssd', bash_command='echo "I/O intensive task"', queue="ssd")

    t_4_cpu = BashOperator(task_id='t_4_cpu', bash_command='echo "CPU instensive task"', queue="cpu_intensive")

    t_5_cpu = BashOperator(task_id='t_5_cpu', bash_command='echo "CPU instensive task"', queue="cpu_intensive")

    t_6_spark = BashOperator(task_id='t_6_spark', bash_command='echo "Spark dependency task"', queue="spark")

    task_7 = EmptyOperator(task_id='task_7')

    [t_1_ssd, t_2_ssd, t_3_ssd, t_4_cpu, t_5_cpu, t_6_spark] >> task_7