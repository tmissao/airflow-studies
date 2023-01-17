FROM apache/airflow:slim-2.5.0-python3.9
RUN pip install --no-cache-dir "apache-airflow[crypto,celery,postgres,cncf.kubernetes,docker]"==2.5.0