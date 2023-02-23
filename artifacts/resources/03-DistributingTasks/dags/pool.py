from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2023, 2, 15),
    'owner': 'Airflow',
    'email': 'owner@test.com'
}

with DAG(dag_id='pool_dag', schedule_interval='0 0 * * *', default_args=default_args, catchup=True) as dag:
    
    # get forex rates of JPY and push them into XCOM
    get_forex_rate_EUR = SimpleHttpOperator(
        task_id='get_forex_rate_EUR',
        method='GET',
        http_conn_id='forex_api',
        endpoint='/latest?base=EUR',
        priority_weight=1,
        pool="forex_api_pool",
        xcom_push=True
    )
 
    # get forex rates of JPY and push them into XCOM
    get_forex_rate_USD = SimpleHttpOperator(
        task_id='get_forex_rate_USD',
        method='GET',
        http_conn_id='forex_api',
        endpoint='/latest?base=USD',
        priority_weight=2,
        pool="forex_api_pool",
        xcom_push=True
    )
 
    # get forex rates of JPY and push them into XCOM
    get_forex_rate_JPY = SimpleHttpOperator(
        task_id='get_forex_rate_JPY',
        method='GET',
        http_conn_id='forex_api',
        endpoint='/latest?base=JPY',
        priority_weight=3
        pool="forex_api_pool",
        xcom_push=True
    )
 
    # Templated command with macros
    bash_command="""
        {% for task in dag.task_ids %}
            echo "{{ task }}"
            echo "{{ ti.xcom_pull(task) }}"
        {% endfor %}
    """

    # Show rates
    show_data = BashOperator(
        task_id='show_result',
        bash_command=bash_command
    )

    [get_forex_rate_EUR, get_forex_rate_USD, get_forex_rate_JPY] >> show_data