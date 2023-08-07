import airflow
from airflow.models import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup

DAG_NAME="task_group"

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

with DAG(dag_id=DAG_NAME, default_args=default_args, schedule_interval="@once") as dag:
    
    start = EmptyOperator(
        task_id='start'
    )

    with TaskGroup(group_id="process_a") as task_group_1:
        for i in range(5):
            EmptyOperator(task_id=f'task-{(i + 1)}')

    some_other_task = EmptyOperator(
        task_id='check'
    )

    with TaskGroup(group_id="process_b") as task_group_2:
        for i in range(5):
            EmptyOperator(task_id=f'task-{(i + 1)}')

    end = EmptyOperator(
        task_id='final'
    )

    start >> task_group_1 >> some_other_task >> task_group_2 >> end