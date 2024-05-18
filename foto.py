# Importación de la excepción personalizada DimensionError desde el archivo error.py
from error import DimensionError

# Definición de la clase Foto
class Foto:
    # Valor máximo determinado por el atributo de clase MAX
    MAX = 2500

    # Constructor de la clase
    def __init__(self, ancho=None, alto=None):
        # Inicialización de atributos protegidos con valores por defecto None
        self._ancho = None
        self._alto = None
        # Si se proporcionan valores de ancho y alto, se asignan utilizando los setters
        if ancho is not None:
            self.ancho = ancho
        if alto is not None:
            self.alto = alto

    # Getter para el atributo ancho
    @property
    def ancho(self):
        return self._ancho

    # Setter para el atributo ancho
    @ancho.setter
    def ancho(self, value):
        # Validación del nuevo valor de ancho, lanzando una excepción si está fuera del rango permitido
        if not (1 <= value <= Foto.MAX):
            raise DimensionError(f"Ancho fuera de rango: {value}. El máximo permitido es {Foto.MAX}", "ancho", Foto.MAX)
        # Si el valor es válido, se asigna al atributo protegido _ancho
        self._ancho = value

    # Getter para el atributo alto
    @property
    def alto(self):
        return self._alto

    # Setter para el atributo alto
    @alto.setter
    def alto(self, value):
        # Validación del nuevo valor de alto, lanzando una excepción si está fuera del rango permitido
        if not (1 <= value <= Foto.MAX):
            raise DimensionError(f"Alto fuera de rango: {value}. El máximo permitido es {Foto.MAX}", "alto", Foto.MAX)
        # Si el valor es válido, se asigna al atributo protegido _alto
        self._alto = value

    # Método para solicitar al usuario las dimensiones de la foto
    def input_dimensiones(self):
        while True:
            try:
                # Solicitar al usuario que ingrese el ancho de la foto
                ancho = int(input("Ingrese el ancho de la foto: "))
                self.ancho = ancho  # Asignar y validar el valor de ancho
                # Solicitar al usuario que ingrese el alto de la foto
                alto = int(input("Ingrese el alto de la foto: "))
                self.alto = alto  # Asignar y validar el valor de alto
                # Mostrar las dimensiones de la foto
                print("Dimensiones de la foto:")
                print("Ancho:", self.ancho)
                print("Alto:", self.alto)
            except ValueError:
                # Capturar y manejar el error si el usuario no ingresa un número entero
                print("Debe ingresar un número entero para las dimensiones.")
            except DimensionError as e:
                # Capturar y manejar el error si las dimensiones están fuera del rango permitido
                print(e)
            
            # Preguntar al usuario si desea agregar otra dimensión
            otra = input("¿Desea agregar otra dimensión? (s/n): ").strip().lower()
            if otra != 's':
                # Salir del bucle si el usuario no desea agregar otra dimensión
                break

# Bloque principal para ejecutar el código solo si se ejecuta el archivo directamente
if __name__ == "__main__":
    # Crear una instancia de la clase Foto
    foto = Foto()
    # Llamar al método input_dimensiones para solicitar las dimensiones al usuario
    foto.input_dimensiones()
