# ----------------------------------------------------------
#
# Emilio Campuzano Mejia A01378948
#
# ----------------------------------------------------------

# NOTA: El siguiente código solo es el esqueleto para inciar el
# proyecto. Los métodos provistos crean la estructura básica con
# todos los objetos que intervienen en el sistema de reservaciones
# de vuelos. Queda pendiente implementar el comportamiento
# descrito en la especificación y añadir la documentación
# correspondiente. Es posible que se requiera añadir nuevos
# métodos y propiedades a las clases definidas a continuación.

from datetime import date


class ReservadorDeVuelos:
    """Instancia de esta clase representa el sistema de
    apartados de vuelos de un aeropuerto
    """

    def __init__(self):
      """Inicializa una Instancia de la clase ReservadorDeVuelos
      """
      self.__vuelos = {}

    def define_vuelo(self,
                     codigo,
                     origen,
                     destino,
                     fecha,
                     num_filas,
                     num_letras):
        """Devuelve todos los datos necesarios para un Vuelo
        en forma de diccionario, para que sea más ordenado
        y para que el sistema tenga un punto de referencia entre
        cada uno. En este caso, el punto de referencia es el
        codigo, que es una serie de letras y números.
        """
        self.__vuelos[codigo] = Vuelo(codigo, origen, destino,
                                      fecha, num_filas, num_letras)

    def imprime_info_vuelo(self, codigo):
        return f"""Vuelo {codigo. } {self.origen}-{self.destino} {self.fecha}"""

    def reserva_vuelo(self, codigo, fila, letra):
        reservation[codigo]=Vuelo(fila, letra)
        if reservation in self.vuelos:
          False
        else:
          True

    def busca_vuelos(self, origen, destino):
        pass


class Vuelo:

    def __init__(self,
                 codigo,
                 origen,
                 destino,
                 fecha,
                 num_filas,
                 num_letras):
        self.__codigo = codigo
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha
        self.__num_filas = num_filas
        self.__num_letras = num_letras

        # Crear las filas de asientos desocupados.
        # A partir de este momento, si queremos
        # acceder al asiento 1A de este vuelo se
        # puede hacer de la siguiente manera:
        #
        #     self.__asientos[1]['A']
        #
        self.__asientos = {}
        for num_fila in range(1, num_filas + 1):
            fila = {}
            for letra in 'ABCDEFGHIJ'[:num_letras]:
                fila[letra] = Asiento()
            self.__asientos[num_fila] = fila


class Asiento:

    def __init__(self):
        self.__ocupado = False