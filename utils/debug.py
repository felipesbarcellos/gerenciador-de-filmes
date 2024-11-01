from loguru import logger


class Debug():
    """Classe com métodos para realizar o debug do software
    de forma planejada
    """
    def __init__(self):
        ...

    def identificar_tipo_de_erro(self, e:Exception):
        """Recebe uma Exception e retorna o
        tipo dela.

        Args:
            e (Exception): Exception a ser inspecionada

        Raises:
            e: Mostra a própria exceção para que o software
            não continue se houver erro.
        """
        logger.error(f"Ocorreu um erro:\n{e}\nTipo do erro:{type(e)}")
        raise e