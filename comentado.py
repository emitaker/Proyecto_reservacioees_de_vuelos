# ----------------------------------------------------------
#
# Emilio Campuzano Mejia A01378948
#
# ----------------------------------------------------------


from datetime import date
import string


class ReservadorDeVuelos:
    """Clase que expone el sistema de apartados para el aeropuerto.
    """

    def __init__(self):
        """Inicializa una Instancia de la clase ReservadorDeVuelos
        """
        # diccionario codigo=>vuelo
        self.__vuelos = {}

    def define_vuelo(self,
                    codigo,
                    origen,
                    destino,
                    fecha,
                    num_filas,
                    num_letras):
        """Crea un vuelo y lo almacena en el diccionario de la instancia.
        """
        # Se validan las entradas utilizando la clase estatica Validador.
        if Validador.vuelo_valido(Validador, codigo, self.__vuelos, origen,
                                    destino, fecha, num_filas, num_letras):
            #Se registra el vuelo en el diccionario.
            self.__vuelos[codigo] = Vuelo(codigo, origen, destino,
                                    fecha, num_filas, num_letras)
        else:
            # Si las entradas no son validas, se dispara un error de ejecución.
            raise RuntimeError

    def imprime_info_vuelo(self, codigo):
        """Imprime todo lo relaciondo con un vuelo, a partir de su codigo
        Los asientos que estan ocupados se representan con una letra
        'X' y los que estan libres con un '.'. Imprime “Código de vuelo
        inexistente” si codigo no existe o es inválido.
        """
        # Se busca el vuelo en el diccionario
        if codigo in self.__vuelos.keys():
            # Se obtiene información del vuelo específico.
            data = self.__vuelos[codigo].flight_data()
            # Se genera la cadena de impresión
            head= f"Vuelo {codigo} {data['origen']}-{data['destino']} "
            head += f"{data['fecha']}\n"
            body = " " + string.ascii_uppercase[0:data["num_letras"]]

            for i in range(data["num_filas"]):
                if i<9 :
                    body += f"\n0{i+1}"
                else:
                    body += f"\n{i+1}"

                for j in range(data["num_letras"]):
                    # se le suma 65 para llegar a la letra 'A' en ascii
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
            if codigo in self.__vuelos.keys():
                vuelo = self.__vuelos[codigo]
                if not [fila,letra] in vuelo.asientos_ocupados:
                    vuelo.asientos_ocupados.append([fila,letra])
                    response = True
        return response

    def busca_vuelos(self, origen, destino):
        """ Devuelve una lista de todos los códigos de los  vuelos válidos que
        van de origen a destino. Si es que no tiene un destino o origen/destino
        son inválidos, regresa una lista vacía
        """
        vuelos_encontrados = []
        for vuelo in self.__vuelos:
            if self.__vuelos[vuelo].origen == origen:
                if self.__vuelos[vuelo].destino == destino:
                    vuelos_encontrados.append(self.__vuelos[vuelo].codigo)
        return vuelos_encontrados

class Vuelo:
    """
    Clase que representa al vuelo, almacena toda la información pertinente
    a un único vuelo.
    """
    def __init__(self,
                codigo,
                origen,
                destino,
                fecha,
                num_filas,
                num_letras):
        #Esta función solo se llama desde define_vuelo.
        #Se valida en define_vuelo
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.__fecha = fecha
        self.__num_filas = num_filas
        self.__num_letras = num_letras
        self.asientos_ocupados = []

    def flight_data(self):
        """
        Este método expone los datos para imprime_info_vuelo
        """
        return {"origen": self.origen,
            "destino": self.destino,
            "fecha": self.__fecha,
            "num_letras": self.__num_letras,
            "num_filas": self.__num_filas,
            "asientos_ocupados": self.asientos_ocupados}

class Validador:
    """
    Clase estatica para revisar que se cumplan las
    condiciones de cada parametro.
    """
    def is_in_list_collector(test_list, in_list):
        """
        Función de utilidad para revisar que todos los elementos en test_list
        esten en in_list.
        Si ese es el caso devuelve True, si no False.
        """
        output = True
        for t in test_list:
            output &= t in in_list
        return output

    def valida_codigo(cls,param,diccionario):
        """
        Revisa que un código es válido y se puede utilizar para  un vuelo.
        """
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

    def letra(param):
        """Valida una letra para la reserva de un vuelo"""
        #letra debe ser una cadena con un solo carácter de una letra
        #mayúscula de la 'A' a la 'J'.
        return isinstance(param, str) and param in string.ascii_uppercase[0:10]


    def valida_origen_destino(cls, param):
        """Revisa que un orige o destino sea valido"""
        #origen y destino deben ser cadenas con exactamente tres letras
        #mayúsculas. Representan códigos de aeropuertos.
        #Un vuelo no puede tener el mismo origen y destino.
        output = False
        if isinstance(param, str) and len(param)==3:
            output = cls.is_in_list_collector(param, string.ascii_uppercase)
        return output


    def valida_fecha(param):
        """Revisa que el parametro de fecha sea una instancia de tipo date"""
        #fecha es una instancia de la clase date del módulo datetime.
        #Representa el año, mes y día en el que sale el vuelo correspondiente.
        return isinstance(param, date)


    def valida_num_filas(param):
        """Revisa que la fila cumple con los requerimientos."""
        #num_filas debe ser un número entero entre 1 y 99.
        return isinstance(param,int) and param > 0 and param < 100


    def valida_num_letras(param):
        """Revisa que la cantidad de letras cumpla con los requerimientos"""
        #num_letras debe ser un número entero entre 1 y 10.
        return isinstance(param,int) and param > 0 and param <11


    def fila(param):
        """Revisa que la fila cumple con los requerimientos."""
        #fila debe ser un número entero entre 1 y 99.
        return isinstance(param,int) and param > 0 and param < 100

    def vuelo_valido(cls,codigo,diccionario,
                origen,
                destino,
                fecha,
                num_filas,
                num_letras):
        """Revisa la validez de todos los parametros de define_vuelo"""
        out = cls.valida_codigo(cls,codigo,diccionario)
        out &= cls.valida_origen_destino(cls,origen)
        out &= cls.valida_origen_destino(cls,destino) and destino != origen
        out &= cls.valida_fecha(fecha)
        out &= cls.valida_num_filas(num_filas)
        out &= cls.valida_num_letras(num_letras)
        return out

    def fila_letra_validas(cls,filaz,letraz):
        """Revisa la validez de al registrar un asiento."""
        return cls.fila(filaz) and cls.letra(letraz)
