from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class Usuario(Base):
    __tablename__ = "usuario"

    usuario_id = Column('usuario_id', Integer, primary_key=True, autoincrement=True)
    nome_de_usuario = Column('nome_de_usuario', String, nullable=False)
    email = Column('email', String, nullable=False)
    password = Column('password', String, nullable=False)

    assistidos = relationship('Assistido', back_populates='usuario')

    def __init__(self, nome_de_usuario, email, password):
        self.nome_de_usuario = nome_de_usuario
        self.email = email
        self.password = password