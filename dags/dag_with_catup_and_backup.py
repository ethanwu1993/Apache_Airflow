from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator




default_args = {
  'owner': 'ethan_wu',
  'retries': 5,
  'retry_delay': timedelta(minutes=2)
}

with DAG(
    'dag_with_catchup_backfill_v02',
    default_args=default_args,
    description='A simple tutorial DAG',
    start_date=datetime(2024, 3, 20),
    schedule_interval="@daily",
    catchup=False
) as dag:
  task1 = BashOperator(
    task_id='first_task',
    bash_command='echo hello world, this is the first task!'
  )

  