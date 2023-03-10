import datetime as dt
from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from docker.types import Mount

dag = DAG(
    dag_id="helloer",
    schedule_interval=dt.timedelta(minutes=10),
    catchup=False,
    start_date=dt.datetime(year=2022, month=1, day=1),
)


helloer = DockerOperator(
    docker_url="unix://var/run/docker.sock",
    image="ghcr.io/1995parham-me/docker:latest",
    command="-c \"echo 'Hi Elahe' > /app/message.txt\"",
    auto_remove=True,
    container_name="hello_my_love",
    mount_tmp_dir=False,
    mounts=[
        Mount(source="/home/parham/Downloads/app", target="/app", type="bind"),
    ],
    task_id="helloer",
    dag=dag,
)
