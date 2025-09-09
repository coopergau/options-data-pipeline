## Things to add to get finished
- airflow
- aws
- add a clean and safe commands.txt file

## Things to make it good
- make sure duplicates arent added to the tables
- handle failures

RDS (Postgres) – managed database, replaces your local Docker DB.
Realistic: no company wants prod data in a Docker container on one laptop.

ECR (Elastic Container Registry) – store your Dockerized Python script.
Realistic: standard way to run custom code in AWS.

MWAA (Airflow) – orchestrator that runs the script every day.
Realistic: industry standard for scheduling pipelines.

Secrets Manager – holds your DB creds.
Professional: avoids hardcoding passwords.

CloudWatch – Airflow/MWAA logs automatically go here.
Practical: how teams debug failed runs.

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
