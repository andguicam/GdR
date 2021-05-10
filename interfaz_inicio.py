from tkinter import *
import sys
from easysnmp import Session
from interfaz_botones import * 



def clear(ventana):
		for widgets in ventana.winfo_children():
			widgets.destroy()

def inicio_session(host, community, estado_checkbox, ventana,app):
	if estado_checkbox.get():
		clear(ventana)
		Label(ventana, text="Lista de agentes", fg="blue", font=("Arial", 12)).grid(row=0, column= 1)
		interfaz_botones(app, None, estado_checkbox)
	else: 
		try:
			session = easysnmp.Session(hostname= host.get(), community=community.get(), version=2)	
			clear(ventana)
			Label(ventana, text="hostname:", fg="blue", font=("Arial", 12)).grid(row=0, column= 1)
			Label (ventana, text=host.get(), fg="blue", font=("Arial", 12)).grid(row=0, column=2)
			Label(ventana, text="community:", fg="blue", font=("Arial", 12)).grid(row=0, column= 3)
			Label(ventana, text=community.get(), fg="blue", font=("Arial", 12)).grid(row=0, column=4)
			interfaz_botones(app, session, estado_checkbox)
		except easysnmp.exceptions.EasySNMPConnectionError: 
			Label(ventana, text="Error en el inicio de session", fg="red").grid(row=6, column=3)
	
	return None



app = Tk() 
app.geometry('600x600')
app.title("Mib-browser")
#creamos un frame para el incio
inicio = Frame(app)
inicio.pack()
#Presentamos una pantalla con los parametro para iniciar session 
Label(inicio, text="Inicio de session", fg="blue", font=("Arial", 16)).grid(row=0, column= 2)
host_var= StringVar()
Label (inicio, text="Introduce la direccion IP: " ).grid(row=1, column=1)
host_entry = Entry (inicio, textvariable=host_var).grid(row=1, column=2)
community_var= StringVar()
Label (inicio, text="Introduce la community: ").grid(row=2, column=1)
community_entry= Entry (inicio, textvariable=community_var).grid(row=2, column=2)
estado_checkbox=BooleanVar()
agentes_checkbox=Checkbutton(inicio,text="Usar lista de agentes",variable=estado_checkbox)
agentes_checkbox.grid(row= 3, column=3)

inicio_boton= Button(inicio, text="Iniciar session", command=lambda: inicio_session(host_var, community_var,estado_checkbox, inicio, app)).grid(row= 6, column=2)


app.mainloop()

