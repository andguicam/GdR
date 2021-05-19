from funciones.tabla_handler import tabla_handler
from tkinter import *
import sys
from types import ClassMethodDescriptorType
from funciones.get_handler import *
from funciones.get_handler import get_handler
from funciones.set_handler import set_handler
from funciones.get_next_handler import get_next_handler
from funciones.limpiar import limpiar
from funciones.presentar_tabla import presentar_tabla
from funciones.traducir_direcciones import presentar_direcciones


def interfaz_botones(app, session):	
		oid_var= StringVar()
		Label (app, text="Introduce el oid: " ).place(x=30, y =50)
		oid_entry= Entry (app, textvariable=oid_var)
		oid_entry.place(x=175, y =50)
		button_set= Button(app, text="Set", command = lambda:set_handler(session,oid_var.get(),campo_respuesta,estado_checkbox,estado_checkbox_exportar))
		button_get=Button(app, text="Get", command = lambda:get_handler(session,oid_var.get(),campo_respuesta,estado_checkbox,estado_checkbox_exportar))
		button_getNext=Button(app, text="Get next", command = lambda:get_next_handler(session,oid_var.get(),campo_respuesta,estado_checkbox,estado_checkbox_exportar))
		button_gettabla = Button (app, text="Tablas", command = lambda: presentar_tabla(session, oid_var.get(), app,campo_respuesta,estado_checkbox_exportar))
		button_traducir = Button(app,text="Traducir",command = lambda: presentar_direcciones (oid_var.get(), campo_respuesta))
		button_set.place(x=30, y=100)
		button_get.place(x=90, y =100)
		button_getNext.place(x=150, y =100)
		button_gettabla.place(x=240, y=100)
		button_traducir.place(x=320, y =100)

		estado_checkbox=BooleanVar()
		agentes_checkbox=Checkbutton(app,text="Usar lista de agentes",variable=estado_checkbox)
		agentes_checkbox.place(x=30,y=150)
		estado_checkbox_exportar=BooleanVar()
		exportar_checkbox=Checkbutton(app,text="Exportar resultado de la operación",variable=estado_checkbox_exportar)
		exportar_checkbox.place(x=30,y=175)

		Label_respuesta = Label(app, text="Respuesta de la operación:")
		Label_respuesta.place(x=30, y=250)
		campo_respuesta = Label(app, text="")
		campo_respuesta.place(x=30, y =300)

		

		#boton de limpieza
		button_limpiar = Button(app, text="Limpiar", bg='red', command = lambda: limpiar(oid_entry, campo_respuesta))
		button_limpiar.place(x=400, y = 50)

		


		return None


