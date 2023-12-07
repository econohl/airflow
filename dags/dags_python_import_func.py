from airflow import DAG
import datetime
import pendulum

from airflow.operators.python import PythonOperator
from common.common_func import get_sftp

# dag_id : python 파일명과 일치하는 것을 권장함. 
# schedule ( clonetab : 분-시간-일-월-요일) / 일요일(0), 월요일(1), .. , 토요일(6)
# start_date : tz="UTC" (9시간 늦음 ==> Asia/Seoul 로 변경 )
# catchup : start_date와 현재일자간의 이전 작업을 실행할 것인지에 대한 옵션 
#   1) false : start_date와 현재일자간의 이전 작업 ( 소급적재 안함 )
#   2) true : start_date와 현재일자간의 이전 작업 ( 소급적재 진행 / 순차적 실행 아님 )
# git status --> git add dags/***.py --> git commit -m "{메시지}" --> git push
# (로컬 Terminal) git pull [ 경로 : /Users/1004811/Startground/airflow/dags ]

# Python 외부함수 호출 [ (plugins>) common.common_func.py ]
with DAG(
    dag_id="dags_python_import_func",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 11, 21, tz="Asia/Seoul"),
    catchup=False,
    tags=["example", "example2"],
    # params={"example_key": "example_value"},
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id='task_get_sftp',
        python_callable=get_sftp
    )