import os
from dotenv import load_dotenv
import psycopg2


HOME = os.getcwd()
load_dotenv(HOME + '/.env')

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = psycopg2.connect(f"host={DB_HOST} dbname={DB_NAME} user={DB_USERNAME} password={DB_USERNAME}")
cur  = conn.cursor()

try:
    with open(f'{HOME}/source/users_w_postal_code.csv','r') as f:
        next(f)
        cur.copy_from(f,'latihan_users',sep=',',columns=('email','name','phone','postal_code'))
    conn.commit()
    print(f'Success')
except ValueError:
    print('Failed')
