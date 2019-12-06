# Proyecto_reservaciones_de_vuelos

De manera individual, diseña y codifica en Python un sistema orientado a objetos que permita realizar reservaciones de vuelos aéreos.

NOTA: El sistema debe estar compuesto por la clase ReservadorDeVuelos y al menos otras dos clases de tu propio diseño.

La clase ReservadorDeVuelos debe definir mínimamente los siguientes métodos que serán revisados a través de pruebas automáticas (puedes añadir métodos adicionales si así lo deseas):

define_vuelo(self, codigo, origen, destino, fecha, num_filas, num_letras): Establece la existencia de un vuelo identificado por codigo, que sale de origen y llega a destino en cierta fecha. Adicionalmente, el vuelo cuenta una cierta cantidad de asientos acomodados en varias filas (num_filas), y cada fila con un cierto número de letras (num_letras). Lanza una excepción de tipo RuntimeError si cualquiera de los argumentos es inválido.

imprime_info_vuelo(self, codigo): Imprime toda la información de un vuelo a partir de su codigo. Los asientos disponibles se indican con un punto (.) y los ocupados con una equis (X). Ver los ejemplos más adelante para conocer el formato exacto de la salida esperada. Imprime “Código de vuelo inexistente” si codigo no existe o es inválido.

reserva_vuelo(self, codigo, fila, letra): Realiza la reservación del vuelo identificado con codigo para el asiento en la posición dada por fila y letra. Devuelve True si se pudo realizar la reservación de manera exitosa, o False si el asiento ya estaba ocupado o si codigo, fila o letra son inexistentes o inválidos.

busca_vuelos(self, origen, destino): Devuelve una lista con todos los códigos de los vuelos que salen de origen y que llegan a destino. Devuelve una lista vacía si no existen vuelos de origen a destino, o si origen y/o destino son inexistentes o inválidos.

Sobre los argumentos de los métodos

Los métodos descritos arriba reciben uno o varios argumentos cuyas restricciones se listan a continuación:

codigo de vuelo debe ser una cadena con exactamente cinco caracteres. Los primeros dos caracteres deben ser letras mayúsculas. Los últimos tres caracteres deben ser dígitos. Cada vuelo debe tener un codigo único el cual no puede ser utilizado por ningún otro vuelo.
origen y destino deben ser cadenas con exactamente tres letras mayúsculas. Representan códigos de aeropuertos. Un vuelo no puede tener el mismo origen y destino.
fecha es una instancia de la clase date del módulo datetime. Representa el año, mes y día en el que sale el vuelo correspondiente.
num_filas debe ser un número entero entre 1 y 99.
num_letras debe ser un número entero entre 1 y 10.
fila debe ser un número entero entre 1 y 99.
letra debe ser una cadena con un solo carácter de una letra mayúscula de la 'A' a la 'J'.
