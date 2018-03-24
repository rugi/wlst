#showenviroment.py
#Muestra las variables de ambiente existentes.
#Se importa la biblioteca de interacción con el sistema operativo.
import os
# Se itera sobre el mapa, mostrando: llave = valor de su contenido
for key, val in os.environ.items():
    print key, '=', val 
