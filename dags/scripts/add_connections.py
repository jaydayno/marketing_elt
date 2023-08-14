from airflow.models.connection import Connection
from dotenv import dotenv_values
from airflow import settings
from pathlib import Path
import logging

path_lib = Path(__file__).parent.parent.resolve()
creds = dotenv_values(f"{path_lib}/configuration.env")

def create_fivetran_connection():
    try:
        print(path_lib)
        conn = Connection(
            conn_id='my_fivetran',
            conn_type='Fivetran',
            login=creds['FivetranAPIKey'],
            password=creds['FivetranAPISecret']
        )
        session = settings.Session()
        session.add(conn)
        session.commit()
        logging.info(f'Added connection: {conn.conn_id}')
    except:
        session.rollback()
        logging.exception(f'Faiiled to establish connection for {conn.conn_id}, rolled back')
    finally:
        session.close()

if __name__ == '__main__':
    create_fivetran_connection()