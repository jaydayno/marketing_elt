airflow-up:
	docker-compose up airflow-init && docker-compose up -d

airflow-down:
	docker-compose down --volumes --rmi all