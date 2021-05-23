from tkinter import *
def limpiar(oid_entry, campo_respuesta): 
	oid_entry.delete(0,'end')
	campo_respuesta.config(text=" ")
def limpiar_campo(campo_respuesta):
	campo_respuesta.config(text=" ")
def limpiar_frame(respuesta_frame):
	respuesta_frame.destroy()