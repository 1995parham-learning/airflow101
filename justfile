default:
    @just --list

# create requirements for docker-compose
env:
    mkdir -p ./dags ./logs ./plugins ./config
    echo -e "AIRFLOW_UID=$(id -u)" > .env

# set up the dev environment with docker-compose
dev cmd *flags:
    #!/usr/bin/env bash
    echo '{{ BOLD + YELLOW }}Development environment based on docker-compose{{ NORMAL }}'
    set -euxo pipefail
    if [ {{ cmd }} = 'down' ]; then
      docker compose down
      docker compose rm
    elif [ {{ cmd }} = 'up' ]; then
      @just env
      docker compose up --wait -d {{ flags }}
    else
      docker compose {{ cmd }} {{ flags }}
    fi
