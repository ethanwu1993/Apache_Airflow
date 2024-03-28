from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import sklearn
import matplotlib

default_args = {
    'owner': 'ethan_wu',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def get_sklearn():
    print(f"sklearn version: {sklearn.__version__}")

def get_mat():
    print(f"mat version: {matplotlib.__version__}")

with DAG(
    'dag_with_python_dependencies_v02',
    default_args=default_args,
    description='A simple tutorial DAG',
    start_date=datetime(2024, 3, 25),
    schedule_interval='0 0 * * *'
) as dag:
    get_sklearn =  python_task = PythonOperator(
        task_id="get_sklearn",
        python_callable=get_sklearn
        # op_kwargs: Optional[Dict] = None,
        # op_args: Optional[List] = None,
        # templates_dict: Optional[Dict] = None
        # templates_exts: Optional[List] = None
    )

    get_mat =  python_task = PythonOperator(
        task_id="get_mat",
        python_callable=get_mat
        # op_kwargs: Optional[Dict] = None,
        # op_args: Optional[List] = None,
        # templates_dict: Optional[Dict] = None
        # templates_exts: Optional[List] = None
    )

    get_sklearn >> get_mat
        