from airflow import DAG
from datetime import datetime, timedelta
from airflow.decorators import dag, task


default_args = {
    'owner': 'ethan_wu',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


@dag(
    dag_id = "dag_with_task_api_v02",
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2024, 3, 23, 10, 45),
)
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            "first_name": "Ethan",
            "last_name" : "Wu"
        }

    @task
    def get_age():
        return 19

    @task
    def greet(first_name, last_name, age):
        print(f"Hello World! My name is {first_name} {last_name}, and I am {age} years old!")

    name_dict = get_name()
    age = get_age()

    greet(first_name=name_dict['first_name'], last_name=name_dict['last_name'], age=age)


greet_dag = hello_world_etl()
