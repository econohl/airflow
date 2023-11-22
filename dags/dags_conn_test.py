from airflow import DAG
import datetime
import pendulum

from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_conn_test",
    schedule="0 11 * * *",
    start_date=pendulum.datetime(2023, 11, 21, tz="Asia/Seoul"),
    catchup=False,
    tags=["dagtest", "dagtest2"],
    # params={"example_key": "example_value"},
) as dag:
    empty_t1 = EmptyOperator(
        task_id="empty_t1" 
    ) 

    empty_t2 = EmptyOperator(
        task_id="empty_t2" 
    )

    empty_t3 = EmptyOperator(
        task_id="empty_t3" 
    ) 

    empty_t4 = EmptyOperator(
        task_id="empty_t4" 
    )

    empty_t5 = EmptyOperator(
        task_id="empty_t5" 
    ) 

    empty_t6 = EmptyOperator(
        task_id="empty_t6" 
    )

    empty_t7 = EmptyOperator(
        task_id="empty_t7" 
    ) 

    empty_t8 = EmptyOperator(
        task_id="empty_t8" 
    )

    empty_t1 >> [empty_t2, empty_t3] >> empty_t4
    empty_t5 >> empty_t4
    [empty_t4,empty_t7] >> empty_t6 >> empty_t8