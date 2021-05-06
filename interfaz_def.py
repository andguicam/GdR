from tkinter import *
import sys
from funciones.get_handler import *
from easysnmp import Session
from funciones.cargar_mibs import *
from funciones.get_handler import get_handler
from funciones.set_handler import set_handler
from funciones.get_next_handler import get_next_handler
from funciones.cargar_mibs import *

#funcion para iniciar session
#creamos una session de snmp
session = Session(hostname='localhost', community='public', version=2)


#creamos la pestaña principal
app = Tk() 
app.geometry('600x600')
app.title("Mib-browser")
parametro = " "
#Seleeciones de mibs disponibles
tabla_mibs=["SNMPv2-MIB","IF-MIB","IP-MIB", "HOST-RESOURCES-MIB"]
value_inside = StringVar(app)
value_inside.set("Selecciona la mib")
mibs_menu = OptionMenu (app, value_inside, *tabla_mibs).pack()
def obtener():
	Label(app, text="Hemos seleccionado la mib: ").pack()
	Label(app, text=value_inside.get()).pack()
	if (value_inside.get() == "SNMPv2-MIB"):
		descr_table = obtener_mib("SNMPv2-MIB")
		#cargamos los valores
		sys_value = StringVar(app)
		sys_value.set("Selecciona un objeto")
		oid = obtener_oid("sysDescr")
		sys_menu = OptionMenu (app, sys_value, *descr_table).pack()
		if (sys_value.get()!="Selecciona un objeto"):
		#buscamos que elemento hemos pulsado para enviar su oid a las funciones get y set
		parametro = obtener_oid(sys_value.get(), "SNMPv2-MIB")
			
		
	else : 
		parametro = " "
	Button (app, text="Obtener", command=obtener).pack()

	#añadimos los botones de get, set y getnext

	bottomframe = Frame(app)
	bottomframe.pack(side=BOTTOM)
	button_set= Button(app, text="Set", command = lambda:set_handler(session,parametro,campo_respuesta,estado_checkbox))
	button_get=Button(app, text="Get", command = lambda:get_handler(session, parametro,campo_respuesta,estado_checkbox))
	button_getNext=Button(app, text="Get next", command = lambda:get_next_handler(session,parametro,campo_respuesta,estado_checkbox))
	button_set.place(x=200, y=450)
	button_get.place(x=250, y =450)
	button_getNext.place(x=300, y =450)


	campo_respuesta = Label(app, text="Respuesta de la operación:")
	campo_respuesta.place(x=0, y=525)

	#Creo el checkbox para hacer seleccionar si la operacion se realiza en el agente proporcionado o en la
	#lista de de agentes que se le pasa

	estado_checkbox=BooleanVar()
	agentes_checkbox=Checkbutton(app,text="Usar lista de agentes",variable=estado_checkbox)
	agentes_checkbox.place(x=0,y=480)

	

Button (app, text="Obtener", command=obtener).pack()




app.mainloop()

