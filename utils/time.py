from datetime import datetime


class Date:
    ...

    def date_str_to_datetime(self, date:str) -> datetime:
        """Recebe uma data em string no formato "dd/mm/aaaa"
        e retorna um datetime"

        Args:
            date (str): "dd/mm/aaaa"

        Returns:
            datetime: datetime com a data inseria
        """
        data = date.split('/')
        dia = data[0]
        mes = data[1]
        ano = data[2]
        return datetime(ano, mes, dia)