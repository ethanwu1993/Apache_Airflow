from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator




default_args = {
  'owner': 'ethan_wu',
  'retries': 5,
  'retry_delay': timedelta(minutes=2)
}

with DAG(
    'our_first_dag_v6',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=None,
    start_date=datetime(2024, 3, 21, 10, 45),
    tags=['example'],
) as dag:
  task1 = BashOperator(
    task_id='first_task',
    bash_command='echo hello world, this is the first task!'
  )

  task2 = BashOperator(
    task_id='second_task',
    bash_command='echo hey, I am task2 and will be running after task1!'
  )

  task3 = BashOperator(
    task_id='third_task',
    bash_command='echo hey, I am task3 and will be running after task1 at same time like task2!'
  )

  task4 = BashOperator(
    task_id='four_task',
    bash_command='echo hey, I am task4'
  )

  

  # task1.set_downstream(task2)
  # task1.set_downstream(task3)

  task1 >> task2
  task1 >> task3
  task2 >> task4

  # task1 >> [task2, task3]