# Error.py
# Definicion de la excepcion personalizada DimensionError
class DimensionError(Exception):

    # Constructor de la excepción con parámetros opcionales dimension y maximo
    def __init__(self, mensaje:str , dimension=None, maximo=None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
        super().__init__(mensaje)

    def __str__(self):
        if self.dimension is not None and self.maximo:
            return f"{self.mensaje} {self.dimension} > {self.maximo}"
        return super().__str__()