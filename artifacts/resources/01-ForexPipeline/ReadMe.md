# Example 01: Forex Pipeline

## Setup Development Environment
---

Since we are using the default(base) image of airflow it requires some system dependencies which can be installed with the following commands

```bash
sudo apt-get install -y --no-install-recommends \
        freetds-bin \
        krb5-user \
        ldap-utils \
        libsasl2-2 \
        libsasl2-modules \
        locales  \
        lsb-release \
        sasl2-bin \
        sqlite3 \
        unixodbc \
        mysql-server \
        libmysqlclient-dev \
        postgresql \
        libsasl2-dev \
        python3-dev \
        libldap2-dev \
        libssl-dev \
        libpq-dev
```

After that install create a python environment

```bash
python -m venv .venv
source .venv/bin/activate
```

> We are using PyEnv to install python 3.7

Download Python [Airflow Constraints](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html#constraints-files) accordanly with the python version that you are using

```bash
wget https://raw.githubusercontent.com/apache/airflow/constraints-2.1.4/constraints-3.7.txt
```

Install AirFlow Extras
```bash
pip install --no-cache-dir "apache-airflow[async,amazon,celery,cncf.kubernetes,docker,dask,elasticsearch,ftp,grpc,hashicorp,http,ldap,google,microsoft.azure,mysql,postgres,redis,sendgrid,sftp,slack,ssh,statsd,virtualenv]"==2.1.4 --constraint ./constraints-3.7.txt"
```

## Setup Connections
---

This Datapipeline utilizes the provider [HTTP](https://airflow.apache.org/docs/apache-airflow-providers-http/stable/connections/http.html) so in order to the DAG fully works it is necessary to create a connection called `FOREX_API` and this is done by setting up the [environment variable](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#storing-connections-in-environment-variables) `AIRFLOW_CONN_FOREX_API` in the docker compose file.

> Keep in mind that environment connections is not displayed in the `airflow UI` neither in `airflow connections list`, in order to troubleshot the connection use the command `airflow connections get <connection-id>`


## Fixing Docker Compose Build
---

```bash
export DOCKER_BUILDKIT=0
export COMPOSE_DOCKER_CLI_BUILD=0
```