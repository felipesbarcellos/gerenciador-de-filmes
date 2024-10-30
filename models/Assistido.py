from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Assistido(Base):
    __tablename__ = "assistido"

    assistido_id = Column('assistido_id', Integer, primary_key=True, autoincrement=True)
    filme_id = Column('filme_id', Integer, ForeignKey('filme.filme_id'))
    usuario_id = Column('usuario_id', Integer, ForeignKey('usuario.usuario_id'))
    assistido_em = Column('assistido_em', DateTime, nullable=False)
    avaliacao = Column('avaliacao', Integer, nullable=True)
    resenha = Column(String)
    
    usuario = relationship('Usuario', back_populates='assistidos')
    filme = relationship('Filme', back_populates='assistidos')

    def __init__(self, assistido_em:datetime, avaliacao:float, resenha:str):
        self.assistido_em = assistido_em
        self.avaliacao = avaliacao
        self.resenha = resenha