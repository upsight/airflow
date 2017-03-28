# Releasing

1. Ensure all desired changes are merged into develop.
2. Bump version in [airflow/version.py](https://stash.eng.upsight.com/projects/TP/repos/incubator-airflow/browse/airflow/version.py#16)
3. Tag release with "vX.Y.Z" and push tag
4. Run TeamCity [job](https://teamcity.eng.upsight.com/viewType.html?buildTypeId=Sandbox_UploadInternalPythonPackage) to upload package to our internal PyPI.
