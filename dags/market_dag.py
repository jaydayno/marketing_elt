from fivetran_provider_async.operators import FivetranOperator
from fivetran_provider_async.sensors import FivetranSensor
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow import DAG
import os

PATH_TO_DBT_PROJECT = f"{os.environ['HOME']}/marketing_elt/market_dbt"
PATH_TO_DBT_VENV = f"{os.environ['HOME']}/marketing_elt/elt_venv/bin/dbt"

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

    ## Task 3 - dbt run and test raw data
    view_raw_data_test = BashOperator(
        task_id='dbt_test_raw_data',
        bash_command='source $DBT_VENV && dbt run -s raw_data && dbt test -s raw_data',
        env={'DBT_VENV': PATH_TO_DBT_VENV},
        cwd=PATH_TO_DBT_PROJECT
    )

#initializing_conns >> [start_Fivetran_connector, check_Fivetran_connector] >> 
view_raw_data_test