# Upsight Airflow

## Setup

You can run off of our forked Airflow repo locally with:

```bash
cd /opt
git clone ssh://git@stash.eng.upsight.com:7999/tp/incubator-airflow.git
cd /opt/airflow-meta
source env/bin/activate
pip install -e /opt/incubator-airflow
```

Changes you make to Airflow likely require a restart of one or more components.

```bash
sudo restart airflow-scheduler
sudo restart airflow-webserver
sudo restart airflow-worker
```
