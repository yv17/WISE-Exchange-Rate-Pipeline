# WISE Exchange Rate Pipeline

Hi there, I am documenting this simple project that got myself started with building pipelines on Airflow in PC environment.

If you are a PC user, I hope you will find this documentation helpful if you were to start learning Airflow as a beginner like me. 

This project enables you to build DAGs to obtain and store daily exchange rate of a currency pair of your choice on WISE.

Prequisite:
1. Install Docker Desktop using the link: https://www.docker.com/products/docker-desktop/
2. Clone this repository
3. Create your WISE account using the link: https://wise.com/


Instructions:
1. Open the Docker Desktop app

2. Open a terminal on your IDE and direct to WISE-Exchange-Rate-Pipeline\docker\airflow and type the following command:

    If it is your first time running, use： 
    ```bash
    docker-compose up airflow-init
    docker-compose up
    ```

    else use:
    ```bash
    docker-compose up -d
    ```

2. Go to your browser and copy the path http://localhost:8080/ on a new tab. Login to your local Airflow server using "airflow" for both the username and password.You should see a DAG named "wise_exchange_rate_dag" on your Airflow server

3. Navigate to Connections on your Airflow server and create a new connection using the following details:

        * name = wise_latest_exchange_rate_api
        * url  = https://api.transferwise.com/v1
        * type = HTTP

4. Go back to your IDE and open the python file named "wise_exchange_rate_dag" in docker\airflow\dags

5. To be continued...

