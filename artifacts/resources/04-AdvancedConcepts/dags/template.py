import sys
import airflow
from airflow import DAG, macros
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

# Would be cleaner to add the path to the PYTHONPATH variable
sys.path.insert(1, '/opt/airflow/dags/scripts')

from process_logs import process_logs_func

TEMPLATED_LOG_DIR = """{{ var.value.source_path }}/data/{{ macros.ds_format(ts_nodash, "%Y%m%dT%H%M%S", "%Y-%m-%d-%H-%M") }}/"""

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False,
            "email_on_failure": False,
            "email_on_retry": False,
            "email": "tiago.missao@host.com",
            "retries": 1
        }

with DAG(dag_id="template_dag", schedule_interval="@daily", default_args=default_args) as dag:
    
    predefined_variables = BashOperator(
        task_id = "testing_predefined_variables",
        bash_command="echo {{ds}}"
    )

    # For Create this variable a ENVIRONMENT VALUE named "AIRFLOW_VAR_CASSADRA_LOGIN" was added in docker-compose
    custom_variables = BashOperator(
        task_id = "testing_custom_variables",
        bash_command="echo {{var.value.cassandra_login}}"
    )

    t0 = BashOperator(
        task_id="t0",
        bash_command="echo {{ ts_nodash }}: {{ macros.ds_format(ts_nodash, '%Y%m%dT%H%M%S', '%Y-%m-%d-%H-%M') }}"
    )

    t1 = BashOperator(
            task_id="generate_new_logs",
            bash_command="./scripts/generate_new_logs.sh",
            params={'filename': 'log.csv'})

    t2 = BashOperator(
           task_id="logs_exist",
           bash_command="test -f " + TEMPLATED_LOG_DIR + "log.csv")

    t3 = PythonOperator(
           task_id="process_logs",
           python_callable=process_logs_func,
           provide_context=True,
           templates_dict={'log_dir': TEMPLATED_LOG_DIR},
           params={'filename': 'log.csv'}
           )

    t0 >> t1 >> t2 >> t3