#Cargamos una clase java para leer más fácilmente el archivo
from java.io import FileInputStream
#leemos el archivo
propInputStream = FileInputStream("domaininfo.properties")
#Creamos un contenedor para el archivo
configProps = Properties()
#Cargamos el archivo
configProps.load(propInputStream)
#Recuperamos los valores del archivo
domainName=configProps.get("domain.server.name")
listenAddress=configProps.get("domain.server.listenaddress")
serverPort=configProps.get("domain.server.port")
#Mostramos los valores recuperados
print 'El nombre del dominio es:', domainName
print 'La direccion de recepcion es:', listenAddress
print 'El puerto del servidor es:', serverPort
