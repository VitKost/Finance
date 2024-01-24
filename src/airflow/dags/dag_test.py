from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from dag_test_main import file_sensing_task, findCSVLoadFile, step2, step3


default_args = {
    'owner': 'vkostyrenko',
    'depends_on_past': False,
    'email': ['vi_ko97@mail.ru'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 2,
    'retry_delay': timedelta(minutes=10)
}


myDag = DAG(
    dag_id='myFirstDag',
    default_args=default_args,
    start_date=datetime(2023, 11, 6),
    schedule=timedelta(days=30),
    description="A sample DAG for demonstration."
    )


task1 = PythonOperator(
    task_id='print_name',
    python_callable=findCSVLoadFile,
    dag=myDag,
    )

task2 = PythonOperator(
    task_id='print_age',
    python_callable=step2,
    dag=myDag,
    )

task3 = PythonOperator(
    task_id='print_dow',
    python_callable=step3,
    dag=myDag,
    )

# task sequence
file_sensing_task >> task1 >> task2 >> task3
