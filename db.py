from sqlalchemy import create_engine#, Table, Column, String, Integer, select, text, MetaData
from utils.constants import DB_URL

engine = create_engine(DB_URL, echo=False)
Session = sessionmaker(bind=engine)

def cria_db():
    Base.metadata.create_all(bind=engine)
