# WISE Exchange Rate Pipeline

Hi there, I documented a simple project of mine here as I am learning how to build data pipelines on Airflow in PC environment.

If you are a PC user, I hope you will find this documentation helpful if you were to learn Airflow as a beginner like me. 

This project enables you to build DAGs to obtain and store daily exchange rate of a currency pair of your choice on WISE.

## Prequisite:
1. Install Python 3.7 and above
2. Install Docker Desktop using the link: https://www.docker.com/products/docker-desktop/
3. Clone this repository
4. Create your WISE account using the link: https://wise.com/


## Instructions:
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

2. Go to your browser and copy the path http://localhost:8080/ on a new tab. Login to your local Airflow server using "airflow" for both the username and password. 
You should see a DAG named "wise_exchange_rate_dag" on your Airflow server

3. Navigate to Connections on your Airflow server and create a new connection using the following details:

    * name = wise_latest_exchange_rate_api
    * url  = https://api.transferwise.com/v1
    * type = HTTP

    <sup>*Check that the connection still exists if your Airflow server is restarted, else the pipeline will fail*</sup>

4. Go back to your IDE and open the python file named "wise_exchange_rate_dag" in docker\airflow\dags. Follow the comments in the codes to customize your currency pairs. You can get your WISE API key on the account [settings](https://wise.com/settings/) page under the API Token section.\
<sup>*Remember to whitelist your IP as well, it could be the IP address has changed if the pipeline fails in the future.*</sup>

5. Run the DAG and you should be able to see the data on the csv file once it succeeds!\
<sup>*Remember that the dates could be not in ascending order as it depends on which date finishes first.*</sup>

## References:
Here are some Airflow tutorial links which I found to be very useful:
    * [Airflow Tutorial Zero to Hero](https://www.youtube.com/watch?v=K9AnJ9_ZAXE) by coder2j
    * [How to start with Apache Airflow in Docker (Windows)](https://medium.com/@garc1a0scar/how-to-start-with-apache-airflow-in-docker-windows-902674ad1bbe) by Oscar Garcia

There is also a list of API on the WISE official website (https://api-docs.transferwise.com/api-reference) that you can play with.

I hope you can get some inspirations from this project and build something fun!



