import sys
from pathlib import Path

# Agregamos la raíz de Airflow (/opt/airflow) al sys.path para encontrar 'etl_weather'
sys.path.append(str(Path(__file__).resolve().parents[1]))

from airflow import DAG
from etl_weather.ETL.load import load_data
from etl_weather.db.config_db import startup
from etl_weather.ETL.extrat import get_weather
from etl_weather.ETL.trasform import parser_data
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.models.taskinstance import TaskInstance

# Definimos las tareas del dag

def parser_data_task(ti: TaskInstance):
    """ Pasa la informacion entre tareas """
    data = ti.xcom_pull(task_ids="extract_data")
    
    parsed = parser_data(data)
    
    return parsed.dict()

def load_data_task(ti: TaskInstance):
    """ Recibe los datos parseados y los carga en la db"""
    data = ti.xcom_pull(task_ids="parser_data")
    load_data(data)
    print("Data cargado con exito")
    

# Definimos los argumentos base de nuestro dag
default_args = {
    "owner": "Weather-ETL",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Definimos el Dag
with DAG(
    dag_id="dag_etl_weather",
    description="ETL que hace web scraping para la recoleccion continua de datos",
    default_args=default_args,
    schedule="@daily", 
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    
    # Definimos las tareas
    
    init_db_task = PythonOperator(
        task_id = "start_up_db",
        python_callable=startup
    )
    
    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=get_weather
    )
    
    trasform_task = PythonOperator(
        task_id="parser_data",
        python_callable=parser_data_task
    )
    
    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load_data_task
    )
    
    # Definimos el orden de ejecucion
    init_db_task >> extract_task >> trasform_task >> load_task 
    