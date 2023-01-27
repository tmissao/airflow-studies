import pendulum
from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator

local_tz = pendulum.timezone("America/Sao_Paulo")

DEFAULT_ARGS = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 20, 7, tzinfo=local_tz),
    'email': 'owner@test.com',
    'retries': 3,
    'retry_delay': timedelta(seconds=30),
}

with DAG(
    dag_id="timezone_brt",
    schedule="0 7 * * *",
    default_args=DEFAULT_ARGS,
) as dag:

    task_1 = EmptyOperator(task_id='task_1')

    # run_dates = dag.get_run_dates(start_date=dag.start_date)
    # next_execution_date = run_dates[-1] if len(run_dates) != 0 else None
    # print('datetime from Python is Naive: {0}'.format(timezone.is_naive(datetime(2023, 1, 20))))
    # print('datetime from Airflow is Aware: {0}'.format(timezone.is_naive(timezone.datetime(2023, 1, 20)) == False))
    # print('[DAG:tz_dag] timezone: {0} - start_date: {1} - schedule_interval: {2} - Last execution_date: {3} - next execution_date {4} in UTC - next execution_date {5} in local time'.format(
    #     dag.timezone, 
    #     dag.default_args['start_date'], 
    #     dag.schedule_interval, 
    #     dag.latest_execution_date, 
    #     next_execution_date,
    #     local_tz.convert(next_execution_date) if next_execution_date is not None else None
    # ))