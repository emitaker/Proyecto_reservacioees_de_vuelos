# ----------------------------------------------------------
#
# Emilio Campuzano Mejia A01378948
#
# ----------------------------------------------------------


from datetime import date
import string


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
        """Imprime todo lo relaciondo con un vuelo, a partir de su codigo
        Los asientos que estan ocupados se representan con una letra
        x y los que estan libres con un (.). Imprime “Código de vuelo
        inexistente” si codigo no existe o es inválido.
        """
        # "Vuelo: codigo , origen-destino , fecha(año,mes dia)"
        if codigo in self.__vuelos.keys():
            data = self.__vuelos[codigo].flight_data()
            head = f"""
                Vuelo: {codigo}
                {data['origen']}-{data['destino']}
                {data['fecha']}\n
            """
            body = "  " + string.ascii_uppercase[0:10]

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
        """Hace la reservacion del vuelo identificando el codigo del asiento
        en la posicion dada por fila y letra. Devuelve True si se pudo
        realizar la reservación de manera exitosa, o False si el
        asiento ya estaba ocupado o si codigo, fila o letra son
        inexistentes o inválidos.
        """
        response = False
        if codigo in self.__vuelos[codigo].keys():
            vuelo = self.__vuelos[codigo]
            #validar letra y fila
            if not (letra,fila) in vuelo.asientos_ocupados:
                vuelos.asientos_ocupados.append((letra,fila))
                response = True
        return response

    def busca_vuelos(self, origen, destino):
        """ Devuelve una lista de todos los codigos de los  vuelos válidos que
        van de origen a destino. Si es que no tiene un destino o origen/destino
        son inválidos, regresa una lista vacía
        """
        vuelos_encontrados = []
        for vuelo in self.__vuelos:
            if vuelo.origen == origen and vuelo.destino == destino:
                vuelos_encontrados.append(vuelo.codigo)
        return vuelos_encontrados

class CodigoHolder:
    """Este método
    """
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

    def flight_data(self): """Este método sirve para que se accese de manera
        pública a todos los datos.
        """
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
        if len(param) == 5:
            (dos, tres) = param[0:2], param[2,4]
        #codigo de vuelo debe ser una cadena con exactamente cinco caracteres.
        #Los primeros dos caracteres deben ser letras mayúsculas.
        #Los últimos tres caracteres deben ser dígitos.
        #Cada vuelo debe tener un codigo único el cual no puede ser
        #utilizado por ningún otro vuelo.

    def letra(param):
        return isinstance(param, str) and param in string.ascii_uppercase[0:10]
        #letra debe ser una cadena con un solo carácter de una letra
        #mayúscula de la 'A' a la 'J'.

    def valida_origen_destino(param):
        v_count = 0
        if isinstance(param, str) and len(param)==3:
            for letter in list(param):
                if letra(letter):
                    v_count += 1
        return v_count == 3

        #origen y destino deben ser cadenas con exactamente tres letras
        #mayúsculas. Representan códigos de aeropuertos.
        #Un vuelo no puede tener el mismo origen y destino.

    def valida_fecha(param):
        return isinstance(param, date)
        #fecha es una instancia de la clase date del módulo datetime.
        #Representa el año, mes y día en el que sale el vuelo correspondiente.

    def valida_num_filas(param):
        return param > 0 and param < 100
        #num_filas debe ser un número entero entre 1 y 99.

    def valida_num_letras(param):
        return param > 0 and param <11
        #num_letras debe ser un número entero entre 1 y 10.

    def fila(param):
        return param > 0 and param < 100
        #fila debe ser un número entero entre 1 y 99.
