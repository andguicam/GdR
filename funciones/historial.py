from datetime import datetime
import time
#La informacion se le pasa en forma de tupla (oid,respuesta,ip)
def historial(lista,tipo_peticion):
    dia = datetime.now()
    hoy = time.localtime()
    hora = time.strftime("%H:%M:%S", hoy)
    fecha = dia.strftime("%d/%m/%y")
    try:
        f = open("logs/log.txt","a")
        for elemento in lista:
            texto="[{0} {1}] Se ha realizado la petición {2} al equipo {3} con OID {4} y respuesta '{5}'".format(
                fecha,hora,tipo_peticion,elemento[2],elemento[0],elemento[1])
            f.write(texto+"\n")
        f.close()
    except:
        print("Error escribiendo en archivo de log.")
        f.close()
