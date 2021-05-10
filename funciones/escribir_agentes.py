from datetime import datetime
import time
def escribir_agentes(lista,oid):
    dia = datetime.now()
    hoy = time.localtime()
    hora = time.strftime("%H-%M-%S", hoy)
    fecha = dia.strftime("%d-%m-%y")
    oid_limpio=oid.replace(".","-")

    f = open("exports/"+oid_limpio+"_"+fecha+"_"+hora+".csv", "w")
    for elemento in lista:
        f.write(elemento[2]+","+elemento[1]+"\n")
    f.close()
