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
        if Validador.vuelo_valido(Validador,codigo,self.__vuelos,origen,destino,fecha,num_filas,num_letras):
            self.__vuelos[codigo] = Vuelo(codigo, origen, destino,fecha, num_filas, num_letras)
        else:
            raise RuntimeError

    def imprime_info_vuelo(self, codigo):
        """Imprime todo lo relaciondo con un vuelo, a partir de su codigo
        Los asientos que estan ocupados se representan con una letra
        x y los que estan libres con un (.). Imprime “Código de vuelo
        inexistente” si codigo no existe o es inválido.
        """
        # "Vuelo: codigo , origen-destino , fecha(año,mes dia)"
        if codigo in self.__vuelos.keys():
            data = self.__vuelos[codigo].flight_data()
            head = f"""Vuelo {codigo} {data['origen']}-{data['destino']} {data['fecha']}\n"""
            body = " " + string.ascii_uppercase[0:data["num_letras"]]

            for i in range(data["num_filas"]):
                if i<9 :
                    body += f"\n0{i+1}"
                else:
                    body += f"\n{i+1}"

                for j in range(data["num_letras"]):
                    #assientos ocupados SET
                    if [i+1,chr(65+j)] in data["asientos_ocupados"]:
                        body += 'X'
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
        if Validador.fila_letra_validas(Validador,fila, letra):
            # raise RuntimeError(f"{fila} {letra}")
            if codigo in self.__vuelos.keys():
                vuelo = self.__vuelos[codigo]
                #validar letra y fila
                if not [fila,letra] in vuelo.asientos_ocupados:
                    vuelo.asientos_ocupados.append([fila,letra])
                    response = True
        return response

    def busca_vuelos(self, origen, destino):
        """ Devuelve una lista de todos los codigos de los  vuelos válidos que
        van de origen a destino. Si es que no tiene un destino o origen/destino
        son inválidos, regresa una lista vacía
        """
        vuelos_encontrados = []
        for vuelo in self.__vuelos:
            if self.__vuelos[vuelo].origen == origen and self.__vuelos[vuelo].destino == destino:
                vuelos_encontrados.append(self.__vuelos[vuelo].codigo)
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
        # validar
            self.codigo = codigo
            self.origen = origen
            self.destino = destino
            self.__fecha = fecha
            self.__num_filas = num_filas
            self.__num_letras = num_letras
            self.asientos_ocupados = []

    def flight_data(self):
        """Este método sirve para que se accese de manera
        pública a todos los datos.
        """
        return {"origen": self.origen,
            "destino": self.destino,
            "fecha": self.__fecha,
            "num_letras": self.__num_letras,
            "num_filas": self.__num_filas,
            "asientos_ocupados": self.asientos_ocupados}

class Validador:
    def is_in_list_collector(test_list, in_list):
        output = True
        for t in test_list:
            output &= t in in_list
        return output

    def valida_codigo(cls,param,diccionario):#IB323
        output = True
        if  isinstance(param, str) and len(param) == 5:
            (dos, tres) = param[0:2], param[2:5]
            output &= cls.is_in_list_collector(dos, string.ascii_uppercase)
            output &= cls.is_in_list_collector(tres, string.digits)
            for key in diccionario:
                if key==param:
                    output = False

        else:
            output = False
        return output
        #codigo de vuelo debe ser una cadena con exactamente cinco caracteres.
        #Los primeros dos caracteres deben ser letras mayúsculas.
        #Los últimos tres caracteres deben ser dígitos.
        #Cada vuelo debe tener un codigo único el cual no puede ser
        #utilizado por ningún otro vuelo.

    def letra(param):
        return isinstance(param, str) and param in string.ascii_uppercase[0:10]
        #letra debe ser una cadena con un solo carácter de una letra
        #mayúscula de la 'A' a la 'J'.

    def valida_origen_destino(cls, param):
        output = False
        if isinstance(param, str) and len(param)==3:
            output = cls.is_in_list_collector(param, string.ascii_uppercase)
        return output

        #origen y destino deben ser cadenas con exactamente tres letras
        #mayúsculas. Representan códigos de aeropuertos.
        #Un vuelo no puede tener el mismo origen y destino.

    def valida_fecha(param):
        return isinstance(param, date)
        #fecha es una instancia de la clase date del módulo datetime.
        #Representa el año, mes y día en el que sale el vuelo correspondiente.

    def valida_num_filas(param):
        return isinstance(param,int) and param > 0 and param < 100
        #num_filas debe ser un número entero entre 1 y 99.

    def valida_num_letras(param):
        return isinstance(param,int) and param > 0 and param <11
        #num_letras debe ser un número entero entre 1 y 10.

    def fila(param):
        #fila debe ser un número entero entre 1 y 99.
        return isinstance(param,int) and param > 0 and param < 100

    def vuelo_valido(cls,codigo,diccionario,
                origen,
                destino,
                fecha,
                num_filas,
                num_letras):
        out = cls.valida_codigo(cls,codigo,diccionario)
        out &= cls.valida_origen_destino(cls,origen)
        out &= cls.valida_origen_destino(cls,destino) and destino != origen
        out &= cls.valida_fecha(fecha)
        out &= cls.valida_num_filas(num_filas)
        out &= cls.valida_num_letras(num_letras)
        return out

    def fila_letra_validas(cls,filaz,letraz):
        return cls.fila(filaz) and cls.letra(letraz)
