import datetime as dt
from typing import Any, Dict
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests

dag = DAG(
    dag_id="ipinfo",
    schedule_interval=dt.timedelta(minutes=10),
    catchup=False,
    start_date=dt.datetime(year=2022, month=1, day=1),
)


def _ipconfig(templates_dict):
    output_file_name = templates_dict["output_file_name"]

    resp = requests.get("https://ipconfig.io/json")
    resp.raise_for_status()
    info: Dict[str, Any] = resp.json()
    with open(output_file_name, "a", encoding="utf-8") as output_file:
        output_file.write(f"{info['ip']} @ {info['country']}")
        output_file.flush()


ipconfig = PythonOperator(
    task_id="request_ip_country",
    python_callable=_ipconfig,
    templates_dict={"output_file_name": "/outputs/{{ ts_nodash }}.txt"},
    dag=dag,
)
