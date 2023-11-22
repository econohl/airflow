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
    empty_t1 = BashOperator(
        task_id="empty_t1" 
    ) 

    empty_t2 = BashOperator(
        task_id="empty_t2" 
    )

    empty_t3 = BashOperator(
        task_id="empty_t3" 
    ) 

    empty_t4 = BashOperator(
        task_id="empty_t4" 
    )

    empty_t5 = BashOperator(
        task_id="empty_t5" 
    ) 

    empty_t6 = BashOperator(
        task_id="empty_t6" 
    )

    empty_t7 = BashOperator(
        task_id="empty_t7" 
    ) 

    empty_t8 = BashOperator(
        task_id="empty_t8" 
    )

    empty_t1 >> [empty_t2, empty_t3] >> empty_t4
    empty_t5 >> empty_t4
    [empty_t4,empty_t7] >> empty_t6 >> empty_t8