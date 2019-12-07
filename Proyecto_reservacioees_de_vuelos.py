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

"""
Criterios de evaluación
(70%) El código pasa todas las pruebas.
(20%) El diseño y la implementación de la solución incluye y utiliza al menos dos clases adicionales a la clase ReservadorDeVuelos.
(10%) El código se apega a las convenciones de codificación del lenguaje Python: 1) nombres de variables/clases/métodos descriptivos; 2) indentación de cuatro espacios por nivel; 3) líneas de texto de menos de 80 caracteres; y 4) métodos y clases incluyen cadena de documentación. Ver: bit.ly/2OKCBSJ
"""

from datetime import date


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
            head = f"""
                Vuelo: {codigo}
                {data['origen']}-{data['destino']}
                {data['fecha']}\n
            """
            body = "  "

            letras = ("A","B","C","D","E","F","G","H","J")
            for z in range(data["num_letras"]):
                body += letras[z]

                for i in range(data["num_letras"]):
                    body += f"\n{i}"
                    for j in range(data["num_filas"]):
                        #assientos ocupados SET
                        if (i,j) in data["asientos_ocupados"]:
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

class CodigoHolder:
    codes = []
    def exists(codigo):
        codigo in codes

class Vuelo:
    #REMINDER runtime error invalid arguments
    def __init__(self,
                codigo,
                origen,
                destino,
                fecha,
                num_filas,
                num_letras):
        # validar madres
        # if not valido: raise RunTimeError("chingo a su madre")
        self.__codigo = codigo
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha
        self.__num_filas = num_filas
        self.__num_letras = num_letras
        # asientos ocupados
        self.__asientos_ocupados = []

    def flight_data(self):
        return {
        "origen": self.__origen,
        "destino": self.__destino,
        "fecha": self.__fecha,
        "num_letras": self.__num_letras,
        "num_filas": self.__num_filas,
        "asientos_ocupados": self.__asientos_ocupados
        }

class Validador:
    def valida_codigo(param):
        pass
        #codigo de vuelo debe ser una cadena con exactamente cinco caracteres. Los primeros dos caracteres deben ser letras mayúsculas. Los últimos tres caracteres deben ser dígitos. Cada vuelo debe tener un codigo único el cual no puede ser utilizado por ningún otro vuelo.


    def valida_origen_destino(param):
        pass
        #origen y destino deben ser cadenas con exactamente tres letras mayúsculas. Representan códigos de aeropuertos. Un vuelo no puede tener el mismo origen y destino.

    def valida_fecha(param):
        pass
        #fecha es una instancia de la clase date del módulo datetime. Representa el año, mes y día en el que sale el vuelo correspondiente.


    def valida_num_filas(param):
        param > 0 and param < 100
        #num_filas debe ser un número entero entre 1 y 99.

    def valida_num_letras(param):
        param > 0 and param <11
        #num_letras debe ser un número entero entre 1 y 10.

    def letra(param):
        pass
        #letra debe ser una cadena con un solo carácter de una letra mayúscula de la 'A' a la 'J'.


    def fila(param):
        param > 0 and param < 100
        #fila debe ser un número entero entre 1 y 99.



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
