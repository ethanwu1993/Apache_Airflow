from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
  'owner': 'ethan_wu',
  'retries': 5,
  'retry_delay': timedelta(minutes=2)
}


with DAG(
  default_args = default_args,
  dag_id = "dag_with_cron_expression_v05",
  start_date=datetime(2024, 3, 20),
  schedule_interval='0 3 * * Tue-Fri'

) as dag:
  task1 = bash_task = BashOperator(
      task_id="bash_task",
      bash_command='echo "Hi from cron expression!"',
      # env: Optional[Dict[str, str]] = None,
      # output_encoding: str = 'utf-8',
      # skip_exit_code: int = 99,
  )