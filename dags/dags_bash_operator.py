

from airflow import DAG
import datetime
import pendulum

from airflow.operators.bash import BashOperator

# dag_id : python 파일명과 일치하는 것을 권장함. 
# schedule ( clonetab : 분-시간-일-월-요일) / 일요일(0), 월요일(1), .. , 토요일(6)
# start_date : tz="UTC" (9시간 늦음 ==> Asia/Seoul 로 변경 )
# catchup : start_date와 현재일자간의 이전 작업을 실행할 것인지에 대한 옵션 
#   1) false : start_date와 현재일자간의 이전 작업 ( 소급적재 안함 )
#   2) true : start_date와 현재일자간의 이전 작업 ( 소급적재 진행 / 순차적 실행 아님 )

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 11 * * *",
    start_date=pendulum.datetime(2023, 11, 21, tz="Asia/Seoul"),
    catchup=False,
    tags=["example", "example2"],
    # params={"example_key": "example_value"},
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2