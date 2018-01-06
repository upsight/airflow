# Changelog

## Next release (in development)

## 1.9.0+up2.0.4

* Quick fix for long lines crashing tasks

## 1.9.0+up2.0.3

* Repatch retrying of SubDAGs ([DATA-3429](https://kontagent.jira.com/browse/DATA-3429))

## 1.9.0+up2.0.2

* Repatch displaying DAG run conf in UI ([DATA-3267](https://kontagent.jira.com/browse/DATA-3267))

## 1.9.0+up2.0.1

* Repatch fetching variable by string in templates ([DATA-2856](https://kontagent.jira.com/browse/DATA-2856))

## 1.9.0+up2.0.0

* Pulled in airflow-1.9.0 ([DATA-3640][https://kontagent.jira.com/browse/DATA-3640])
* Update version so that it adheres to [PEP 440](https://www.python.org/dev/peps/pep-0440/)

## 1.8.2-up1.15.0

* Pulled in [AIRFLOW-1559](https://issues.apache.org/jira/browse/AIRFLOW-1559) ([DATA-3676](https://kontagent.jira.com/browse/DATA-3676))

## 1.8.2-up1.14.0

* Display DAG run conf in the graph UI view ([DATA-3267](https://kontagent.jira.com/browse/DATA-3267))

## 1.8.2-up1.13.0

* Pulled in [AIRFLOW-1627](https://issues.apache.org/jira/browse/AIRFLOW-1627) ([DATA-3500](https://kontagent.jira.com/browse/DATA-3500))

## 1.8.2-up1.12.0

* Pulled in [AIRFLOW-1614](https://issues.apache.org/jira/browse/AIRFLOW-1614) ([DATA-3490](https://kontagent.jira.com/browse/DATA-3490))

## 1.8.2-up1.11.0

* Pulled in [AIRFLOW-1059](https://issues.apache.org/jira/browse/AIRFLOW-1059), [AIRFLOW-1112](https://issues.apache.org/jira/browse/AIRFLOW-1112), [AIRFLOW-1334](https://issues.apache.org/jira/browse/AIRFLOW-1334), and [AIRFLOW-1345](https://issues.apache.org/jira/browse/AIRFLOW-1345) from upstream ([DATA-3487](https://kontagent.jira.com/browse/DATA-3487))
* Pulled in [AIRFLOW-903](https://issues.apache.org/jira/browse/AIRFLOW-903) ([DATA-3488](https://kontagent.jira.com/browse/DATA-3488))

## 1.8.2-up1.10.0

* Pulled in apache-airflow-1.8.2 ([DATA-3085](https://kontagent.jira.com/browse/DATA-3085))

## 1.8.1-up1.9.0

* Ensure UI always shows logs for the latest attempt in UI ([DATA-3439](https://kontagent.jira.com/browse/DATA-3439))

## 1.8.1-up1.8.0

* Fix retrying for SubDagOperator task instances ([DATA-3429](https://kontagent.jira.com/browse/DATA-3429))

## 1.8.1-up1.7.0

* Include base DAG folder in template search path ([DATA-3074](https://kontagent.jira.com/browse/DATA-3074))

## 1.8.1-up1.6.0

* Show hostname on top navigation bar, colored based on environment ([DATA-3064](https://kontagent.jira.com/browse/DATA-3064))
* Airflow version link on About page should go to changelog in Stash for that tag ([DATA-3064](https://kontagent.jira.com/browse/DATA-3064))

## 1.8.1-up1.5.0

* Pulled in apache-airflow-1.8.1 ([DATA-2826](https://kontagent.jira.com/browse/DATA-2826))
* Split flower dependency from celery to avoid version conflicts with forked celery ([DATA-2984](https://kontagent.jira.com/browse/DATA-2984))

## 1.8.0-up1.4.0

* Use forked celery-4.0.2-up1.0.0 ([DATA-2883](https://kontagent.jira.com/browse/DATA-2883))
* Make sure Flask log server is killed at the start of a worker shutdown ([DATA-2897](https://kontagent.jira.com/browse/DATA-2897))

## 1.8.0-up1.3.0

* Make use of Stats+Bucky tag support ([DATA-2853](https://kontagent.jira.com/browse/DATA-2853))
* Support fetching of variables in templates by string ([DATA-2856](https://kontagent.jira.com/browse/DATA-2856))

## 1.8.0-up1.2.0

* Added support for `--hostname` when running worker ([DATA-2817](https://kontagent.jira.com/browse/DATA-2817))

## 1.8.0-up1.1.0

* Pulled in airflow-1.8.0 (no changes from rc5)
* Added Sentry integration ([DATA-2733](https://kontagent.jira.com/browse/DATA-2733))
* Fixed SQL alchemy warning about IN-predicate with empty sequence ([DATA-2819](https://kontagent.jira.com/browse/DATA-2819))

## 1.8.0rc5-up1.0.0

* Pulled in airflow-1.8.0rc5
* Ensured virtualenv is always used ([DATA-2767](https://kontagent.jira.com/browse/DATA-2767))
* Reduced dependency list ([DATA-2772](https://kontagent.jira.com/browse/DATA-2772))
