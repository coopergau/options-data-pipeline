# Options Chain Data Pipeline

## Table of Contents
- [Overview](#overview)
- [Pipeline Features](#pipeline-features)
- [Visuals](#visuals)

## running docker
### install
sudo apt update
sudo apt install -y docker.io docker-compose-v2
sudo usermod -aG docker ubuntu

docker --version
docker compose version

check what the above does

### run airflow

docker compose build
docker compose run --rm airflow-webserver airflow db init
docker compose up -d
docker compose ps

have to create user
docker compose run --rm airflow-webserver airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

connect to EC2
ssh -i ~/options-server-key-pair.pem -L 8080:localhost:8080 ubuntu@54.146.213.0
