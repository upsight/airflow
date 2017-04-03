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

## Releasing

1. Ensure all desired changes are merged into develop.
2. Bump version in [airflow/version.py](https://stash.eng.upsight.com/projects/TP/repos/incubator-airflow/browse/airflow/version.py#16)
3. Tag release with "vX.Y.Z" and push tag
4. Run TeamCity [job](https://teamcity.eng.upsight.com/viewType.html?buildTypeId=Sandbox_UploadInternalPythonPackage) to upload package to our internal PyPI.

## Changelog

See [CHANGELOG.md](https://stash.eng.upsight.com/projects/TP/repos/incubator-airflow/browse/upsight/CHANGELOG.md)
