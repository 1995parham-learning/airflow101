<h1 align="center">
  <a href="https://github.com/apache/airflow/">Apache Airflow</a> 101
</h1>

<p align="center">
  <img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/1995parham-learning/airflow101?style=for-the-badge&logo=python">
</p>

## Introduction

We are going to review Apache Airflow features and use it to develop and monitor workflows.
In order to examine source codes, you first need to have an instance of airflow:

```bash
just dev up

# username: airflow
# password: airflow
```

You can maintain DAGs in `/dags` and have access to its UI at `127.0.0.1:8080`.

## Using it with Docker Operator

For having Docker operator in Airflow we need to pass Docker's socket into docker:

```
/var/run/docker.sock
```

This socket belongs to root user and docker group, but we don't have either of these in Airflow container
so, we need to give read and write access to others for this socket.

```bash
sudo chmod o+rw /var/run/docker.sock
```
