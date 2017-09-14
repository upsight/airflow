# Changelog

## Next release (in development)

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
