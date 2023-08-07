# Security at Airflow

## Storing Sensitive Data
---
By default Airflow handles a lot of sensitive information, and stores than in the database. In order to keep these sensitive information secure, it is necessary always run airflow with the `crypto` library.

In order to store sensitive information on database Airflow uses a `FERNET_KEY`. The fernet key guarantees that a password encrypted using it cannot be manipulated or read without the key.

For more details of how generate, and configure a custom fernet key look at this [documentation](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/security/secrets/fernet.html).


## Hiding Variables Values
---

In order to prevent a variable to be displayed on the UI, airflow provides a list of sensitive names, meaning that if you variable contains one of this names the value will not be displayed in the UI.

The default values are:

- access_token
- api_key
- apikey
- authorization
- passphrase
- passwd
- password
- private_key
- secret
- token

For more details look at this [documentation](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/security/secrets/mask-sensitive-values.html).