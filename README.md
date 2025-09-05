## Things to add to get finished
- airflow
- aws
- change this line when its on aws in docker-compose.yaml:       AIRFLOW__WEBSERVER__SECRET_KEY: "my-example-project-secret-key-12345"


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