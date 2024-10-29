from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    ...

class Filme(Base):
    __tablename__ = "filmes"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    assistido_em = Column('assistido_em', String, nullable=True)

    def __init__(self, nome, assistido_em):
        self.nome = nome
        self.assistido_em = assistido_em