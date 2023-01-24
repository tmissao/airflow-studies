# DAG
 DAG stands up to Direct Acycle Graph and it represents the data pipeline

 ```python
from airflow import DAG
from datetime import datetime, timedelta

DEFAULT_ARGS = {
    "owner" : "airflow",
    "email_on_failure" : False,
    "email_on_retry" : False,
    "email" : "admin@localhost.com.br",
    "retries" : 3,
    "retry_delay" : timedelta(minutes=1),
}

with DAG(
    dag_id="forex_data_pipeline",
    schedule=datetime(2023, 1, 1),
    schedule_interval="@daily",
    default_args=DEFAULT_ARGS,
    catchup=False
) as dag:
    # some tasks (operators) here! 
 ```

 ## Relationship Between Operators
 ---

 In order to setup dependencies between Tasks in your DAG it is utilized the operator `>>`(mother of) and `<<` (children of)

 ```python
    with DAG(
        dag_id="forex_data_pipeline",
        schedule=datetime(2023, 1, 1),
        schedule_interval="@daily",
        default_args=DEFAULT_ARGS,
        catchup=False
    ) as dag:

    forex_processing = SparkSubmitOperator(
        task_id="forex_processing",
        conn_id="spark_conn",
        application="/opt/airflow/dags/scripts/forex_processing.py",
        verbose=False
    )

    send_email_notification = EmailOperator(
        task_id="send_email_notification",
        to="t.missao@gmail.com",
        subject="forex_data_pipeline",
        html_content="<h3>forex_data_pipeline</h3>"
    )

    send_slack_notification = SlackWebhookOperator(
        task_id='send_slack_notification',
        http_conn_id='slack_conn',
        message=_get_message(),
        channel="#monitoring"
    )

    forex_processing >> send_email_notification # same as forex_processing.set_dowstream(send_email_notification)
    send_email_notification >> send_slack_notification
 ```

 ## References
 ---

 - [`DAG Model`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/dag/index.html#airflow.models.dag.DAG)