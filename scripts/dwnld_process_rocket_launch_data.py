import json
import pathlib 
import airflow
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def _get_pictures(pic_dir):
    """
    Parameters
    ------------
    pic_dir
    """
    pathlib.Path()

def main():
    dag = DAG(
            dag_id="download_rocket_launches",
            start_data=airflow.utils.dates.days_ago(14),
            schedule_interval=None,

            )
    
    download_launches = BashOperator(
            task_id="download_launches",
            bash_command="curl -o /tmp/launches.json 'https://
            ll.thespacedevs.com/2.0.0/launch/upcoming'",
            dag=dag,

            )


