import pandas as pd


# CSV 불러오기
df = pd.read_csv("inactive_economy.csv", header=0)  # 첫 번째 행을 컬럼명으로 강제 지정

# 컬럼명이 제대로 설정되었는지 확인
print(df.head())

# CSV 파일을 다시 저장 (첫 번째 행이 컬럼명이 되도록)
df.to_csv("inactive_economy_fixed.csv", index=False, encoding="utf-8")

import pymysql
import pandas as pd

# MySQL 연결 함수
def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        db="your_database",
        charset="utf8"
    )
    return conn

# MySQL에서 데이터를 가져와 DataFrame으로 변환하는 함수
def fetch_data(query):
    conn = get_connection()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute(query)
    rows = cur.fetchall()
    df = pd.DataFrame(rows)
    cur.close()
    conn.close()
    return df