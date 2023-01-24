# Operators
---

On Airflow all operators inheritances from the meta class [BaseOperatorMeta](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/baseoperator/index.html#airflow.models.baseoperator.BaseOperatorMeta) and all [default_args](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/baseoperator/index.html#airflow.models.baseoperator.BaseOperatorMeta) passed to DAG instance creations are sent to operators

## Type of Operators
---
Currently there are 3 types of operators in Airflow

1. `Action` - Performs Actions
2. `Transfer` - Transfers data from a source to a destination
3. `Sensor` - Awaits a conditions in order to fire up

## Reference
---

- [`AirFlow Core Operators`](https://airflow.apache.org/docs/apache-airflow/stable/operators-and-hooks-ref.html)
