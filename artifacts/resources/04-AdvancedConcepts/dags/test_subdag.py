import airflow
from subdags.subdag import factory_subdag
from airflow.models import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.subdag import SubDagOperator
from airflow.executors.sequential_executor import SequentialExecutor

DAG_NAME="test_subdag"

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

with DAG(dag_id=DAG_NAME, default_args=default_args, schedule_interval="@once") as dag:
    start = EmptyOperator(
        task_id='start'
    )

    subdag_1 = SubDagOperator(
        task_id='subdag_1',
        subdag=factory_subdag(DAG_NAME, 'subdag_1', default_args),
    )

    some_other_task = EmptyOperator(
        task_id='check'
    )

    subdag_2 = SubDagOperator(
        task_id='subdag_2',
        subdag=factory_subdag(DAG_NAME, 'subdag_2', default_args),
    )

    end = EmptyOperator(
        task_id='final'
    )

    start >> subdag_1 >> some_other_task >> subdag_2 >> end