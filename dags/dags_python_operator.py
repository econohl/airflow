from airflow import DAG
import datetime
import pendulum

from ariflow.operator.python import PythonOperator
import random

# dag_id : python 파일명과 일치하는 것을 권장함. 
# schedule ( clonetab : 분-시간-일-월-요일) / 일요일(0), 월요일(1), .. , 토요일(6)
# start_date : tz="UTC" (9시간 늦음 ==> Asia/Seoul 로 변경 )
# catchup : start_date와 현재일자간의 이전 작업을 실행할 것인지에 대한 옵션 
#   1) false : start_date와 현재일자간의 이전 작업 ( 소급적재 안함 )
#   2) true : start_date와 현재일자간의 이전 작업 ( 소급적재 진행 / 순차적 실행 아님 )
# git status --> git add dags/***.py --> git commit -m "{메시지}" --> git push
# (로컬 Terminal) git pull [ 경로 : /Users/1004811/Startground/airflow/dags ]

# Python Operator [ ariflow.operator.python ]
# 1. PythonOperator : 어떤 파이썬 함수를 실행시키기 위ㄴ 오퍼레이터 
# 1. BranchPythonOperator : 파이썬 함수 실행 결과에 따라 task를 선택적으로 실행시킬 때 사용되는 오퍼레이터 

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 11, 21, tz="Asia/Seoul"),
    catchup=False,
    tags=["example", "example2"],
    # params={"example_key": "example_value"},
) as dag:
    def select_fruit():    # 파이썬 함수 [ def 예약어 ]
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rand_int = random.randint(0,3)
        print(fruit[rand_int])

    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit
    )

    py_t1