from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.empty import EmptyOperator

DEFAULT_ARGS = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 25)
}

with DAG(
    dag_id="project_ignore",
    schedule="0 * * * *", # same result
    default_args=DEFAULT_ARGS,
) as dag:

    task_1 = EmptyOperator(task_id='task_1')
    
    task_2 = EmptyOperator(task_id='task_2')

    task_1 >> task_2

    run_dates = dag.get_run_dates(start_date=dag.start_date)
    next_execution_date = run_dates[-1] if len(run_dates) != 0 else None
    print('[DAG:start_and_schedule_dag] start_date: {0} - schedule_interval: {1} - Last execution_date: {2} - next execution_date {3} in UTC'.format(
        dag.default_args['start_date'], 
        dag.schedule_interval, 
        dag.latest_execution_date, 
        next_execution_date
    ))