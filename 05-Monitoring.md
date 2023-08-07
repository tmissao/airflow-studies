# Monitoring - Logs

The airflow log system is configured using python log library and has many useful capabilities as send log to:

- console
- file
- stream
- [elasticsearch](https://airflow.apache.org/docs/apache-airflow-providers-elasticsearch/stable/logging/index.html)
- [s3](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/logging/s3-task-handler.html)
- [azure blob](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/logging/index.html)

Most of the custom log capabilities requires an overwrite of the [airflow's log configuration](https://github.com/apache/airflow/blob/main/airflow/config_templates/airflow_local_settings.py) and for that it is necessary:

1. irflow’s logging system requires a custom .py file to be located in the **PYTHONPATH**, so that it’s importable from Airflow. Start by creating a directory to store the config file, `$AIRFLOW_HOME/config` is recommended.

2. Create empty files called `$AIRFLOW_HOME/config/log_config.py` and `$AIRFLOW_HOME/config/__init__.py`.

3. Copy the contents of `airflow/config_templates/airflow_local_settings.py` into the `log_config.py` file created in Step 2.

4. Perform the customization

> In order to know if the configuration is working check the logs of the scheduler


# Monitoring - Metrics

In order to leverage information about metrics, airflow uses another tool called `StatsD`. Metrics are based on three types

- Counters
- Gauges
- Timers

> In order to push airflow metrics it is necessary to `install statsD`

All metrics provided by airflow could be accessed [here](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html)