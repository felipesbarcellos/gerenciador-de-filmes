from sqlalchemy import insert, select
from db import engine
from models.Filme import Filme
from sqlalchemy.orm import Session


class ControllerFilmes():
    def __init__(self, view):
        self.view = view
        ...

    def get_filmes(self, limit=10, offset=0):
        with Session(engine) as s:
                # print(filmes.columns)
                filmes = s.scalars(
                    select(Filme)
                    .limit(limit)
                    .offset(offset)
                    )
                return filmes.fetchall()

    def adicionar_filme(self, nome, assistido_em=None):
        with Session(engine) as s:
            filme = Filme(nome=nome, assistido_em=assistido_em)
            s.add(filme)
            s.commit()

    def atualizar_lista_filmes(self):
         filmes = self.get_filmes()
         self.view.atualizar_lista(filmes)
