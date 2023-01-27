import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

HOME = os.getcwd()
load_dotenv(HOME + '/.env')


DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")



try:
    conn = create_engine(f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    print(f'Connection to {conn} Success')
except ValueError:
    print('Connection Failed')


# curr = conn.execute("SELECT * FROM public.users;")
# print(curr.fetchall())


# fetch dataframe
query = """
SELECT * FROM public.users;
"""

df = pd.read_sql_query(query, conn )
print(df)
