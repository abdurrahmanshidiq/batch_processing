import os
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


HOME = os.getcwd()
load_dotenv(HOME + '/.env')

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


file_path = rf"{HOME}/source/users_w_postal_code.csv"
file_name = os.path.basename(file_path).split(".")[0]

df = pd.read_csv(file_path, sep=',')
df['email'] =  df['email'].apply(lambda x: x.split('@')[0])


# engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
engine = create_engine(f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
# conn = engine.connect()

df.to_sql(file_name, engine, if_exists='replace')

#print(df)