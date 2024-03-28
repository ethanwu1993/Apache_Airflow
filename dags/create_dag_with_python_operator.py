from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator

default_args = {
  'owner': 'Ethan',
  'retries': 5,
  'retry_delay': timedelta(minutes=5)
}


def greet(ti):
  first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
  last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
  age = ti.xcom_pull(task_ids='get_age', key='age')
  print(f"Hello World! My name is {first_name} {last_name}, and I am {age} years old.")


def get_name(ti):
  ti.xcom_push(key='first_name', value='Jerry')
  ti.xcom_push(key='last_name', value='Fridman')


def get_age(ti):
  ti.xcom_push(key='age', value=22)
  

with DAG(
    'our_dag_with_python_operator_v06',
    default_args=default_args,
    description='Our first using python operator',
    schedule_interval='@daily',
    start_date=datetime(2024, 3, 23, 10, 45),
    
) as dag:
  
  task1 = PythonOperator(
      task_id="greet",
      python_callable=greet,
      # op_kwargs = { "age": 20}
      # op_args: Optional[List] = None,
      # templates_dict: Optional[Dict] = None
      # templates_exts: Optional[List] = None
  )


  task2 = PythonOperator(
      task_id="get_name",
      python_callable=get_name,
      # op_kwargs: Optional[Dict] = None,
      # op_args: Optional[List] = None,
      # templates_dict: Optional[Dict] = None
      # templates_exts: Optional[List] = None
  )

  task3 = python_task = PythonOperator(
      task_id="get_age",
      python_callable=get_age,
      # op_kwargs: Optional[Dict] = None,
      # op_args: Optional[List] = None,
      # templates_dict: Optional[Dict] = None
      # templates_exts: Optional[List] = None
  )

  [task2, task3] >> task1