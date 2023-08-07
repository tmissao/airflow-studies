import airflow
import requests
from airflow.models import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup


default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}


with DAG(dag_id='trigger_rules_dag', 
    default_args=default_args, 
    schedule_interval="@once") as dag:

  with TaskGroup(group_id="download_website") as download:
    download_website_a = BashOperator(task_id="download_website_a", bash_command='exit 1')
    download_website_b = BashOperator(task_id="download_website_b", bash_command='exit 1')
  
  download_failed = EmptyOperator(task_id="download_failed", trigger_rule="all_failed")
  download_succeed = EmptyOperator(task_id="download_succeed", trigger_rule="all_success")
  process = EmptyOperator(task_id="process", trigger_rule="one_success")
  notify_success = EmptyOperator(task_id="notify_success", trigger_rule="none_failed")
  notify_failed = EmptyOperator(task_id="notify_failed", trigger_rule="one_failed")


  download >> [download_failed, download_succeed] >> process >> [notify_failed, notify_success]
