from datetime import datetime
import time
import csv
def exportar_tabla(lista,oid):
    dia = datetime.now()
    hoy = time.localtime()
    hora = time.strftime("%H-%M-%S", hoy)
    fecha = dia.strftime("%d-%m-%y")
    oid_limpio = oid.replace(".", "-")

    with open("exports/"+oid_limpio+"_"+fecha+"_"+hora+".csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lista)
