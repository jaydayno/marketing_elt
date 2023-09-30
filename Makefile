airflow-up:
	docker-compose up airflow-init && docker-compose up -d

airflow-down:
	docker-compose down --volumes --rmi all

dbt-up:
	docker pull ghcr.io/dbt-labs/dbt-bigquery:1.5.6

dbt-down:
	docker image rm ghcr.io/dbt-labs/dbt-bigquery:1.5.6	