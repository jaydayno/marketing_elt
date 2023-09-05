airflow-up:
	docker-compose up airflow-init && docker-compose up -d

airflow-down:
	docker-compose down --volumes --rmi all

dbt-up:
	docker pull ghcr.io/dbt-labs/dbt-bigquery:1.5.6 && \
	docker run \
		--network=host \
		-v /home/linuxjayday/Desktop/marketing_elt/market_dbt:/usr/app,rshared \
		-v /home/linuxjayday/.dbt:/root/.dbt,rshared \
		ghcr.io/dbt-labs/dbt-bigquery:1.5.6 \
	ls

dbt-down:
	docker image rm ghcr.io/dbt-labs/dbt-bigquery:1.5.6