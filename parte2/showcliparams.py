 #Importamos la biblioteca de sys
import sys

print '--- Revisando los parametros pasados desde la invocacion ---'
size = len(sys.argv)
print 'Tamaño del arreglo;', size
for i in range(0, size):
    print 'Indice ',i,'=',sys.argv[i]

print ""
print 'El primer elemento es el nombre del script',sys.argv[0]
