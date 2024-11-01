import os

DB_URL = "sqlite:///meubanco.db"
SECRET_KEY = 'dev'
INPUT_ETL = os.path.join('data','Filmes.md')
OUTPUT_ETL = os.path.join('data','filmes.csv')