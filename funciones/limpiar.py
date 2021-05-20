from tkinter import *
def limpiar(oid_entry, campo_respuesta): 
	oid_entry.delete(0,'end')
	for widgets in campo_respuesta.winfo_children():
		widgets.destroy()
def limpiar_campo(campo_respuesta):
	for widgets in campo_respuesta.winfo_children():
		widgets.destroy()
def limpiar_frame(respuesta_frame):
	respuesta_frame.destroy()