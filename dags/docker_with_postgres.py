from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator


default_args = {
    'owner': 'ethan_wu',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    'dag_with_postgres_operator_v03',
    default_args=default_args,
    description='A simple tutorial DAG',
    start_date=datetime(2024, 3, 25),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = PostgresOperator(
        task_id = "create_postgres_table",
        postgres_conn_id='postgres_localhost',
        sql="""
            create table if not exists dag_runs (
                dt date,
                dag_id character varying,
                primary key (dt, dag_id)
            )
            """
    )

    task3 = PostgresOperator(
        task_id = "delete_postgres_table",
        postgres_conn_id='postgres_localhost',
        sql="""
            delete from dag_runs
             where dt='{{ ds }}' and dag_id='{{dag.dag_id}}'
            
            """
    )


    
    task2 = PostgresOperator(
        task_id = "insert_postgres_table",
        postgres_conn_id='postgres_localhost',
        sql="""
            insert into dag_runs
             (dt, dag_id)
             values (
            '{{ ds }}', '{{dag.dag_id}}'
            )
            """
    )

    task1 >> task3 >> task2