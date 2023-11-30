from airflow import DAG
import datetime
import pendulum

from airflow.operators.email import EmailOperator

# dag_id : python 파일명과 일치하는 것을 권장함. 
# schedule ( clonetab : 분-시간-일-월-요일) / 일요일(0), 월요일(1), .. , 토요일(6)
# start_date : tz="UTC" (9시간 늦음 ==> Asia/Seoul 로 변경 )
# catchup : start_date와 현재일자간의 이전 작업을 실행할 것인지에 대한 옵션 
#   1) false : start_date와 현재일자간의 이전 작업 ( 소급적재 안함 )
#   2) true : start_date와 현재일자간의 이전 작업 ( 소급적재 진행 / 순차적 실행 아님 )
# git status --> git add dags/***.py --> git commit -m "{메시지}" --> git push
# (로컬 Terminal) git pull [ 경로 : /Users/1004811/Startground/airflow/dags ]

# Google Email 세팅 : Google 홈 > (성현) 클릭 > google 계정관리 > [왼쪽 Tree] 보안 > 
#                    Google에 로그인하는 방법 - 2단계 인증 > 앱 비밀번호 [ lvei zbio ljye cmsw ]

with DAG(
    dag_id="dags_email_operator",
    schedule="0 11 * * *",
    start_date=pendulum.datetime(2023, 11, 30, tz="Asia/Seoul"),
    catchup=False,
    tags=["example", "example2"],
    # params={"example_key": "example_value"},
) as dag:
    send_email_task = EmailOperator(
        task_id="send_email_task",
        to='econohl@hanmail.net',
        subject='Airflow 성공메일',
        html_content="Airflow 작업이 완료되었습니다."
    )