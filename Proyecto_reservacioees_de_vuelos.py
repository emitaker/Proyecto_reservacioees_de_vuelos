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

# tech debt :
# Vuelo constructor
# Validador ??
# Vuelo.flight_data
# Vuelo.asientos ocupados !!es lista

class ReservadorDeVuelos:

    def __init__(self):
        self.__vuelos = {}

    def define_vuelo(self,
                     codigo,
                     origen,
                     destino,
                     fecha,
                     num_filas,
                     num_letras):
        self.__vuelos[codigo] = Vuelo(codigo, origen, destino,
                                      fecha, num_filas, num_letras)

    def imprime_info_vuelo(self, codigo):
		# "Vuelo: codigo , origen-destino , fecha(año,mes dia)"
		if codigo in self.__vuelos.keys():
		    data = self.__vuelos[codigo].flight_data()
			head = f"Vuelo: {data.codigo} {data.origen}-{data.destino} {data.fecha}\n"
			#data.{asientos_ocupados [],num_letras (genera letras),num_filas(genera nums)}
			body = "  "

			letras = ("A","B","C","D","E","F","G","H","J")
			for z in range(data.num_letras):
                body += letras[z]

			for i in range(data.num_letras):
				body += f"\n{i}"
				for j in range(data.num_filas):
					#assientos ocupados SET
					if (i,j) in asientos_ocupados:
						body += 'x'
					else:
                        body += '.'
			print(head, body)

		else:
			print("Código de vuelo inexistente")

    def reserva_vuelo(self, codigo, fila, letra):
		response = False
        if codigo in self.__vuelos[codigo].keys():
			vuelo = self.__vuelos[codigo]
			#validar letra y fila
			if not (letra,fila) in vuelo.asientos_ocupados:
				vuelos.asientos_ocupados.append((letra,fila))
				response = True
		return response

    def busca_vuelos(self, origen, destino):
        vuelos_encontrados = []
		for vuelo in self.__vuelos:
			if vuelo.origen == origen and vuelo.destino == destino:
				vuelos_encontrados.append(vuelo.codigo)
		return vuelos_encontrados



class Vuelo:

	#REMINDER runtime error invalid arguments
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

"""
Vuelo IB323 OAX-MEX 2019-12-07
  ABCD
01....
02.X..
03...X
04....
05....
06....
07....
08....
09....
10....
11....
12....
"""
