from fivetran_provider_async.operators import FivetranOperator
from fivetran_provider_async.sensors import FivetranSensor
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow import DAG

default_args = {
    'owner':'jayden'
}

with DAG( 
    default_args=default_args,
    dag_id='market_elt_dag',
    start_date=datetime.today(),
    schedule=None, #i.e. only manual runs
    catchup=False
) as dag:
    
    # ## Task 0 - Creating Connections in Airflow
    # initializing_conns = BashOperator(
    #     task_id='connection_task',
    #     bash_command='python3 ${AIRFLOW_HOME}/dags/scripts/add_connections.py'
    # )

    # ## Task 1 - Run Fivetran Connector
    # start_Fivetran_connector = FivetranOperator(
    #     task_id='trigger_fivetran',
    #     connector_id='abrasive_elevate', # from Fivetran
    #     fivetran_conn_id='my_fivetran' # from Task 0 i.e. Airflow Connection
    # )

    # ## Task 2 - Check if gone_formalities ran successfully
    # check_Fivetran_connector = FivetranSensor(
    #     task_id='sense_fivetran',
    #     connector_id='abrasive_elevate',
    #     fivetran_conn_id='my_fivetran'
    # )

    # Task 3 - dbt run and test raw data
    view_raw_data_test = DockerOperator(
        task_id='dbt_test_raw_data',
        image='ghcr.io/dbt-labs/dbt-bigquery:1.5.6',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        auto_remove='success',
        command='test -s raw_data'
    )

#initializing_conns >> [start_Fivetran_connector, check_Fivetran_connector] >> 
view_raw_data_test

##!/bin/bash cd usr/app && 
#dbt run -s raw_data && dbt test -s raw_data