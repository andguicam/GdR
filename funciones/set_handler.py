import easysnmp
from pysnmp import hlapi
import tkinter as tk
from funciones.quicksnmp import set
from funciones.leer_agentes import leer_agentes
from funciones.ventana_resultados import ventana_resultados
from easysnmp import Session
#Recibe como parámetro la sesión y el OID (y la ventana), y actualiza la ventana con la respuesta

def set_handler(sesion,oid,etiquetaRespuesta,estado_checkbox):

    #Creamos una ventana con un campo para pedir el valor a introducir

    ventana=tk.Tk()
    ventana.geometry("300x100")
    ventana.title("Introduzca un valor")
    campoTexto=tk.Entry(ventana)
    campoTexto.pack()
    tk.Button(ventana,text="OK",command=lambda:peticion_set(sesion, oid, etiquetaRespuesta,campoTexto.get(),ventana,estado_checkbox)).pack()



def peticion_set(sesion, oid, etiquetaRespuesta,valor,ventana,estado_checkbox):


    if estado_checkbox.get():
            #hay que hacer varias peticiones. Los resultados se devolverán en una lista (de tuplas)
            lista = []
            ventana.destroy()
            agentes = leer_agentes()
            for agente in agentes:
                ip = agente[0]
                comunidad = agente[1].replace("\n", "")
                lista.append(peticion_set_checkbox(ip, comunidad, oid,valor))
            #imprimimos los resultados en una ventana aparte
            ventana_resultados(lista)

    else:
        #Comprobamos que se ha pasado un OID
        if oid:
            try:
                #Obtengo el valor que ha introducido el usuario y elimino la ventana
                ventana.destroy()
                #Realizo peticion y obtengo los valores
                ip = sesion.hostname
                comunidad = sesion.community
                set_response = set(ip, {str(oid): str(valor)},
                                hlapi.CommunityData(comunidad))
                datos = list(set_response.items())
                oid = datos[0][0]
                valor = datos[0][1]
                #Actualizamos la etiqueta referente al campo de respuestas para mostrar el resultado de la operacion
                etiquetaRespuesta.config(
                    text="Respuesta de {0}: '{1}'".format(oid, valor), bg="SpringGreen2")
            except:
                #En caso de excepcion significa que no se ha encontrado el OID solicitado
                etiquetaRespuesta.config(
                    text="El OID introducido no se ha encontrado", bg="red3")
        else:
            print("Tienes que introducir un OID")


def peticion_set_checkbox(ip, comunidad, oid,valor):
    try:
        sesion = Session(hostname=ip, community=comunidad, version=2)
        set_response = set(ip, {str(oid): str(valor)}, hlapi.CommunityData(comunidad))
        datos = list(set_response.items())
        oid = datos[0][0]
        valor = datos[0][1]
        return (oid,valor,ip)
    except:
        return (oid, "Error en la petición",ip)
