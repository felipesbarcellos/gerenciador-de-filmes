from datetime import datetime
import os
from utils.constants import INPUT_ETL, OUTPUT_ETL
from utils.debug import Debug
from utils.time import Date
import pandas as pd


class MD_to_DataFrame():
    """Reads a MD file as input and create an dataframe that can be
    saved as csv.\n
    The MD file must be the exact same way as the example
    found in the example.md
    """
    def __init__(self, input_file):
        self.input_file = input_file
        self.linhas = self._get_linhas()
        self.df = self._linhas_para_dataframe()
        
    def save_df(self, output_file):
        self.df.to_csv(output_file)

    def _get_linhas(self, md_path: os.path):
        """Lê um arquivo e retorna as linhas dele em forma de string

        Args:
            md_path (os.path | str): the path to the .md file to read.
        """
        with open(md_path, mode='r', encoding='utf-8') as f:
            self.linhas = f.readlines()

    def _linhas_para_dataframe(self):
        self._tipo: str                        # Filme ou Série
        self._nome:str                         # Nome do filme
        self._assistido_em: datetime | None    # Data da visualização
        self._genero:str                       # Genero do filme (apenas 1)

        self._tipos: list[str] = [] # Lista que formará a série tipos
        self._nomes: list[str] = [] # Lista que formará a série nomes
        self._assistidos: list[datetime | None] = [] # Lista que formará a série assistidos
        self._generos: list[str] = [] # Lista que formará a série generos

        # Para cada linha no arquivo de lido
        for linha in self.linhas:
            self.linha = linha.replace('\n', '')
            try:
                self._trata_item(linha)
            except Exception as e:
                Debug().identificar_tipo_de_erro(e)
            try:
                self._adicionar_item_na_lista()

                # logger.debug(f'{"-"*SEP_LEN}\nLinha:\n{item}\n{"-"*SEP_LEN}')
            except:
                ...
        data = self._lista_para_dicionario()

        return pd.DataFrame(data)


    def _trata_item(self):
        # Hierarquia dos tipos
        if (self.linha.startswith('### ')):
            self._tipo = self._linha.split(' ')[1].lower()

        # Hierarquia dos generos
        elif(self._linha.startswith('#### ')): 
            self._genero = ' '.join(self._linha.split(' ')[1:])

        # Hierarquia dos não assistidos
        elif(self._linha.startswith('- [ ] ')):
            self._nome = ' '.join(self._linha.split(' ')[3:])
            self._assistido_em = None

        # Hierarquia dos assistidos
        elif(self._linha.startswith('- [x] ')):
            self._linha = ' '.join(self._linha.split(' ')[2:])
            self._nome = self._linha.split(' - ')[0]
            self._assistido_em = self._linha.split(' - ')[1]

            # Verifica se é possível dividir a data em duas e 
            # pega a última pois algumas datas tem inicio e fim
            try:
                self._assistido_em = self._assistido_em.split(' a ')[1]
                if self._assistido_em != 'NA':
                    self._assistido_em = Date().date_str_to_datetime(self._assistido_em)
                else:

                    self._assistido_em = None
            except:
                ...

    def _lista_para_dicionario(self):
        data = {
            'self._tipo': self._tipos,
            'self._nome': self._nomes,
            'self._assistido_em': self._assistidos,
            'self._genero': self._generos
        }
        
        return data

    def _adicionar_item_na_lista(self):
        if self._nome != '':
            self._item = {
                        'self._tipo': self._tipo,
                        'self._nome': self._nome,
                        'self._assistido_em': self._assistido_em,
                        'self._genero': self._genero
                    }

                    
            self._tipos.append(self._item['self._tipo'])
            self._nomes.append(self._item['self._nome'])
            self._assistidos.append(self._item['self._assistido_em'])
            self._generos.append(self._item['self._genero'])

            self._nome = ''