import tkinter as tk
import sys
from easysnmp import Session



from funciones.get_handler import get_handler


if len(sys.argv)!=3:
    print("Tienes que introducir la IP del agente y el nombre de la comunidad\n\
Ejemplo de ejecución: python3 interfazsimple.py 192.168.0.20 public")
    sys.exit()



ip=sys.argv[1]
community=sys.argv[2]


try:
    sesion = Session(hostname=ip, community=community, version=1)
except:
    print("No se ha podido conectar con el agente SNMP. Por favor revisa los parámetros introducidos.")


ventana=tk.Tk()
ventana.geometry("640x360")
ventana.title("GdR prueba GET")

campoTexto = tk.Entry(ventana)
campoTexto.pack()


boton = tk.Button(ventana, text="GET", command=lambda:get_handler(sesion,campoTexto,etiqueta))
boton.pack()

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()
ventana.mainloop()
