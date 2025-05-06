default:
    @just --list

# create requirements for docker-compose
env:
    #!/usr/bin/env bash
    mkdir -p ./dags ./logs ./plugins ./config
    echo -e "AIRFLOW_UID=$(id -u)" > .env

# seed airflow.cfg with default values in config folder.
config:
    docker compose run airflow-cli airflow config list

# initialize database
database-init:
    docker compose up airflow-init

# set up the dev environment with docker-compose
dev cmd *flags:
    #!/usr/bin/env bash
    echo '{{ BOLD + YELLOW }}Development environment based on docker-compose{{ NORMAL }}'
    set -euxo pipefail
    if [ {{ cmd }} = 'down' ]; then
      docker compose down --volumes --remove-orphans
    elif [ {{ cmd }} = 'up' ]; then
      just env
      just config
      just database-init
      docker compose up --wait -d {{ flags }}
      docker compose run airflow-worker airflow info
    else
      docker compose {{ cmd }} {{ flags }}
    fi
