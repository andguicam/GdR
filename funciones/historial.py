from datetime import datetime
import time
import socket
#La informacion se le pasa en forma de tupla (oid,respuesta,ip)
def historial(lista,tipo_peticion):
    dia = datetime.now()
    hoy = time.localtime()
    hora = time.strftime("%H:%M:%S", hoy)
    fecha = dia.strftime("%d/%m/%y")

    #Creamos socket UDP para lanzar una peticion cualquiera, lo que nos
    #permite conocer la direccion ipv4 del equipo
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("1.1.1.1", 80))
        ipv4=s.getsockname()[0]
        s.close()
    except:
        #No se pudo determinar la ipv4 del equipo
        ipv4='que no se pudo determinar'
    
    try:
        f = open("logs/log.txt","a")
        for elemento in lista:
            texto="[{0} {1}] Se ha realizado desde el equipo con IP {6} la petición {2} al agente {3} con OID {4} y respuesta '{5}'".format(
                fecha,hora,tipo_peticion,elemento[2],elemento[0],elemento[1],ipv4)
            f.write(texto+"\n")
        f.close()
    except:
        print("Error escribiendo en archivo de log.")
        f.close()
