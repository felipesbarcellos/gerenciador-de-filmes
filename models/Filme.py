from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Filme(Base):
    __tablename__ = "filme"

    filme_id = Column('filme_id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    genero = Column('genero', String, nullable=False)
    criado_em = Column('criado_em', DateTime, default=datetime.now)

    assistidos = relationship('Assistido', back_populates='filme')

    def __init__(self, nome, assistido_em, genero):
        self.nome = nome
        self.assistido_em = assistido_em
        self.genero = genero