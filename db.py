from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine#, Table, Column, String, Integer, select, text, MetaData
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from utils.constants import DB_URL

class Base(DeclarativeBase):
    ...

# engine = create_engine(DB_URL, echo=False)
db = SQLAlchemy(model_class=Base)
Session = sessionmaker(bind=db)

def cria_db():
    Base.metadata.create_all(bind=db)
