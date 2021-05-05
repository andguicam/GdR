from tkinter import *
import sys
from funciones.get_handler import *
from easysnmp import Session
from funciones.cargar_mibs import *
from funciones.get_handler import get_handler
from funciones.set_handler import set_handler
from funciones.get_next_handler import get_next_handler


#funcion para iniciar session
#creamos una session de snmp
session = Session(hostname='localhost', community='public', version=2)


#creamos la pestaña principal
app = Tk() 
app.geometry('600x600')
app.title("Mib-browser")

#Seleeciones de mibs disponibles
tabla_mibs=["SNMP-V2","IF-MIB" , "IP-MIB", "HOST-RESOURCES-MIB"]
value_inside = StringVar(app)
value_inside.set("Selecciona la mib")
mibs_menu = OptionMenu (app, value_inside, *tabla_mibs).pack()
def obtener():
	Label(app, text="Hemos seleccionado la mib: ").pack()
	Label(app, text=value_inside.get()).pack()
	if (value_inside.get() == "SNMP-V2"):
		system = system_mib()
		#cargamos los valores
		sys_value = StringVar(app)
		sys_value.set("Selecciona un objeto")
		sys_menu = OptionMenu (app, sys_value, *system).pack()
		#valor que se pasa a las funciones de los botones
		parametro = sys_value.get()
	else : 
		parametro = " "
	#añadimos los botones de get, set y getnext
	bottomframe = Frame(app)
	bottomframe.pack(side=BOTTOM)
	button_set= Button(app, text="Set", command = lambda:set_handler(session,parametro,campo_respuesta))
	button_get=Button(app, text="Get", command = lambda:get_handler(session, parametro,campo_respuesta))
	button_getNext=Button(app, text="Get next", command = lambda:get_next_handler(session,parametro,campo_respuesta))
	button_set.place(x=200, y=450)
	button_get.place(x=250, y =450)
	button_getNext.place(x=300, y =450)

	campo_respuesta = Label(app, text="Respuesta de la operación:")
	campo_respuesta.place(x=0, y=500)
	
Button (app, text="Obtener", command=obtener).pack()




app.mainloop()
