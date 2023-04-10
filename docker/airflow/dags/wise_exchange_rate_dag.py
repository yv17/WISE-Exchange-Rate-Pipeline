import os
import csv
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator

def save_exchange_rate(ti) -> None:
    exchg_rate = ti.xcom_pull(task_ids = ['get_latest_exchange_rate'])
    exchg_rate_dict = exchg_rate[0][0]
 
    with open('./plugins/gbp2myr.csv', 'a') as f: #feel free to rename the csv in the plugins folder and remember to change it here too
        w = csv.writer(f)

        if f.tell() == 0:
                w.writerow(exchg_rate_dict.keys())

        w.writerow(exchg_rate_dict.values())

default_args = {
    'owner': '{insert your windows username here}',
    'retries':'1',
    'retry_delay': timedelta(minutes=1)
}

# connection defined in http_conn_id = https://api.transferwise.com/v1
# url = connection + endpoint

with DAG(
    dag_id='wise_exchange_rate_dag',
    default_args=default_args,
    description='to fetch daily exchange rate from WISE',
    start_date=datetime(2022,1,31,0), # you can change the backfill dates here
    schedule_interval='@daily'
) as dag:

    # connection defined in http_conn_id = https://api.transferwise.com/v1
    # connection type = HTTP
    # remember to redefine connection if docker yaml file has been changed
    # url = connection + endpoint

    task_is_wise_api_active=HttpSensor(
        task_id='is_wise_api_active',
        http_conn_id='wise_latest_exchange_rate_api',
        endpoint='rates?source=GBP&target=MYR&time=+{{ ds }}'+'T00:00:00',
        headers= {'Authorization': 'Bearer insert your api key from WISE account here'} 
        # replace the sentence "insert your api key from WISE account here" with your WISE api key. Do not remove the word Bearer
    )

    task_get_latest_exchange_rate=SimpleHttpOperator(
        task_id='get_latest_exchange_rate',
        http_conn_id='wise_latest_exchange_rate_api',
        endpoint='rates?source=GBP&target=MYR&time=+{{ ds }}'+'T00:00:00',
        headers= {'Authorization': 'Bearer insert your api key from WISE account here'},
        method='GET',
        response_filter=lambda response: response.json(),
        log_response=True
    )

    task_save_exchange_rate=PythonOperator(
        task_id='save_exchange_rate',
        python_callable = save_exchange_rate,
        provide_context = True
    )

    task_is_wise_api_active >> task_get_latest_exchange_rate
    task_get_latest_exchange_rate >> task_save_exchange_rate

    # extra notes:
    # Run docker-compose up -d in ../docker/airflow to start the container
    # Run docker-compose down -v in ../docker/airflow to stop the container
    # Username: airflow
    # Password: airflow