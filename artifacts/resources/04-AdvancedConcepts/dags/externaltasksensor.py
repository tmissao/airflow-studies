import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    }

with DAG(dag_id="externaltasksensor_dag", default_args=default_args, schedule_interval="@daily") as dag:
    sensor = ExternalTaskSensor(
        task_id='sensor',
        external_dag_id='sleep_dag',
        external_task_id='t2'    
    )

    last_task = EmptyOperator(task_id="last_task")

    sensor >> last_task