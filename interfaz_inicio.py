from tkinter import *
import sys
from easysnmp import Session
import easysnmp
from funciones.interfaz_botones import *
estado_checkbox=""

def clear(ventana):
		for widgets in ventana.winfo_children():
			widgets.destroy()

def inicio_session(host, community, ventana,app):
	global estado_checkbox
	#si no se introducen los datos 
	if (host.get()=="" or community.get()==""):
		Label(ventana, text="Introduce los datos", fg="red",bg='snow').grid(row=6, column=3)
	else : 
		try:
			session = easysnmp.Session(hostname= host.get(), community=community.get(), version=2)	
			clear(ventana)
			Label(ventana, text="hostname:", fg="blue", font=("Arial", 12),bg='snow').grid(row=0, column= 2)
			Label (ventana, text=host.get(), fg="blue", font=("Arial", 12),bg='snow').grid(row=0, column=3)
			Label(ventana, text="community:", fg="blue", font=("Arial", 12),bg='snow').grid(row=0, column= 4)
			Label(ventana, text=community.get(), fg="blue", font=("Arial", 12),bg='snow').grid(row=0, column=5)
			estado_checkbox=interfaz_botones(app, session)
		except easysnmp.exceptions.EasySNMPConnectionError: 
			Label(ventana, text="Error en el inicio de sesión", fg="red").grid(row=6, column=3)
		
	return None



app = Tk() 
app.geometry('600x560')
app.title("Mib-browser")
app.configure(bg='snow')
#creamos un frame para el incio
inicio = Frame(app)
inicio.configure(bg='snow')
inicio.pack()
#Presentamos una pantalla con los parametro para iniciar session 
Label(inicio, text="Inicio de sesión", fg="blue", font=("Arial", 16),bg='snow').grid(row=0, column= 2)
host_var= StringVar()
Label (inicio, text="Introduce la dirección IP: " ,bg='snow').grid(row=1, column=1)
host_entry = Entry (inicio, textvariable=host_var,bg='snow').grid(row=1, column=2)
community_var= StringVar()
Label (inicio, text="Introduce la community: ",bg='snow').grid(row=2, column=1)
community_entry= Entry (inicio, textvariable=community_var,bg='snow').grid(row=2, column=2)
#TODO: Esto es una chapuza que se me ha ocurrido para solucionarlo de manera temporal
#y que no se descuadre todo
Label(inicio,text="                                         ",bg='snow').grid(row=0,column=3)

inicio_boton= Button(inicio, text="Iniciar sesión", command=lambda: inicio_session(host_var, community_var, inicio, app),fg='snow').grid(row= 6, column=2)


app.mainloop()

