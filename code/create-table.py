import os
from dotenv import load_dotenv
import psycopg2
import csv


HOME = os.getcwd()
load_dotenv(HOME + '/.env')

print(HOME)
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

#connect to potsgresql
try:
    conn = psycopg2.connect(f"host={DB_HOST} dbname={DB_NAME} user={DB_USERNAME} password={DB_USERNAME}")
    print(f'Connection to {conn} Success')
except ValueError:
    print('Connection Failed')

cur  = conn.cursor()
  
#create table 
cur.execute("""
            CREATE TABLE IF NOT EXISTS latihan_users(
                id serial PRIMARY KEY,
                email text,
                name text,
                phone text,
                postal_code text)
"""
)

with open(f'{HOME}/source/users_w_postal_code.csv') as f:
    # print(f.readlines())
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader) #skip header
    for row in csv_reader:
        cur.execute("INSERT INTO latihan_users VALUES ( default, %s, %s, %s,%s) ON CONFLICT DO NOTHING", row)
    
conn.commit()


# cur.execute("INSERT INTO latihan_users VALUES (%s, %s, %s, %s,%s)", (1, 'hello@dataquest.io', 'Some Name','621234413', '12343'))
# conn.commit()
# print("Create Table Success")