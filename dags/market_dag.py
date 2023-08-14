from fivetran_provider_async.operators import FivetranOperator
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
    
    ## Task 0 - Creating Connections in Airflow
    initializing_conns = BashOperator(
        task_id = 'connection_task',
        bash_command= 'python3 ${AIRFLOW_HOME}/dags/scripts/add_connections.py'
    )

initializing_conns