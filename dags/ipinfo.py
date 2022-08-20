import datetime as dt
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests

dag = DAG(
    dag_id="ipinfo",
    schedule_interval=dt.timedelta(minutes=10),
    catchup=False,
    start_date=dt.datetime(year=2022, month=1, day=1),
)


def _ipconfig():
    resp = requests.get("https://ipconfig.io/country")
    resp.raise_for_status()
    with open("/outputs/country", "r") as output_file:
        output_file.write(f"{resp.text}\n")
        output_file.flush()


ipconfig = PythonOperator(
    task_id="request_ip_country",
    python_callable=_ipconfig,
    dag=dag,
)
