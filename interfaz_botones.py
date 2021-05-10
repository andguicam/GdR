from tkinter import *
import sys
from funciones.get_handler import *
from funciones.get_handler import get_handler
from funciones.set_handler import set_handler
from funciones.get_next_handler import get_next_handler

def interfaz_botones(app, session, estado_checkbox):	
	if (session !=None):
		oid_var= StringVar()
		Label (app, text="Introduce el oid: " ).place(x=150, y =100)
		oid_entry= Entry (app, textvariable=oid_var).place(x=258, y =100)
		button_set= Button(app, text="Set", command = lambda:set_handler(session,oid_var.get(),campo_respuesta,estado_checkbox))
		button_get=Button(app, text="Get", command = lambda:get_handler(session,oid_var.get(),campo_respuesta,estado_checkbox))
		button_getNext=Button(app, text="Get next", command = lambda:get_next_handler(session,oid_var.get(),campo_respuesta,estado_checkbox))
		button_set.place(x=220, y=200)
		button_get.place(x=270, y =200)
		button_getNext.place(x=320, y =200)
		Label_respuesta = Label(app, text="Respuesta de la operación:")
		Label_respuesta.place(x=50, y=300)
		campo_respuesta = Label(app, text=" ")
		campo_respuesta.place(x=50, y =350)
	else: 
		button_set= Button(app, text="Set", command = lambda:set_handler(session,None,None,estado_checkbox))
		button_get=Button(app, text="Get", command = lambda:get_handler(session,None,None,estado_checkbox))
		button_getNext=Button(app, text="Get next", command = lambda:get_next_handler(session,None,None,estado_checkbox))
		button_set.place(x=220, y=200)
		button_get.place(x=270, y =200)
		button_getNext.place(x=320, y =200)