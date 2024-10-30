from sqlalchemy import select
from db import Session
from models.filme import Filme


class ControllerFilmes():
    def __init__(self):
        ...

    def get_filmes(self, limit=10, offset=0):
        with Session() as s:
                # print(filmes.columns)
                filmes = s.scalars(
                    select(Filme)
                    .limit(limit)
                    .offset(offset)
                    )
                return filmes.fetchall()

    def adicionar_filme(self, nome, assistido_em=None):
        with Session() as s:
            filme = Filme(nome=nome, assistido_em=assistido_em)
            s.add(filme)
            s.commit()

    def atualizar_lista_filmes(self):
         filmes = self.get_filmes()
         self.view.atualizar_lista(filmes)
