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

# assign directory
directory = f'{HOME}/source'
for files in os.listdir(directory):
    
    file_path = os.path.join(directory,files)
    file_name = os.path.basename(file_path).split(".")[0]
    
    if os.path.isfile(file_path):
       print(file_name)
       df = pd.read_csv(file_path, sep=',') 
       if("email") in df:
           df['email'] =  df['email'].apply(lambda x: x.split('@')[0])
       engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
       df.to_sql(file_name,engine,if_exists='replace')