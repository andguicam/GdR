from tkinter import *
from easysnmp import Session
import sys
#definicion de funciones para la obtencion de mibs
#creamos una sesion en snmp
session = Session(hostname='localhost', community='public', version=2)
def obtener_mib (mib):
	session = Session(hostname='localhost', community='public', version=2)
	system_items = session.walk(mib)
	system_dic ={}
	#vamos a crear un diccionario para cada oid de system 
	for item in system_items:
		system_dic[item.oid]= [item.snmp_type, item.value]
	#for key in system_dic:
		#print (key, ":", system_dic[key])
	return system_dic
#############################################################################
#Creamos la pestaña principal
app = Tk() 
app.geometry('300x200')
app.title("Mib-browser")
#llamamos a la funcion para obentener las mibs de system
system_dic = obtener_mib('system')
#presentamos en la app los resultados obtenidos
for key in system_dic:
	Label (app, text= key).pack()
app.mainloop()

