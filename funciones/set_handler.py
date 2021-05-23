import easysnmp
from pysnmp import hlapi
import tkinter as tk
import re
from funciones.traducir_direcciones import traducir_direcciones
from funciones.quicksnmp import set
from funciones.leer_agentes import leer_agentes
from funciones.ventana_resultados import ventana_resultados
from easysnmp import Session
from funciones.historial import historial
from funciones.escribir_agentes import escribir_agentes
#Recibe como parámetro la sesión y el OID (y la ventana), y actualiza la ventana con la respuesta


def set_handler(sesion, oid, etiquetaRespuesta, estado_checkbox, estado_checkbox_exportar):

    #Creamos una ventana con un campo para pedir el valor a introducir
    #traducimos el oid si este es no numerico
    
    ventana=tk.Tk()
    ventana.geometry("300x100")
    ventana.title("Introduzca un valor")
    campoTexto=tk.Entry(ventana)
    campoTexto.pack()
    tk.Button(ventana,text="OK",command=lambda:peticion_set(sesion, oid, etiquetaRespuesta,campoTexto.get(),ventana,estado_checkbox,estado_checkbox_exportar)).pack()



def peticion_set(sesion, oid, etiquetaRespuesta,valor,ventana,estado_checkbox,estado_checkbox_exportar):
    lista_parametro=[]

    if estado_checkbox.get():
        #hay que hacer varias peticiones. Los resultados se devolverán en una lista (de tuplas)
        lista = []
        ventana.destroy()
        agentes = leer_agentes()
        for agente in agentes:
            ip = agente[0]
            comunidad = agente[1]
            lista.append(peticion_set_checkbox(ip, comunidad, oid,valor))
        #imprimimos los resultados en una ventana aparte
        # Ventana resultados ya imprime la impresion en el archivo de log
        ventana_resultados(lista, "SET")
        if estado_checkbox_exportar.get():
            escribir_agentes(lista, oid)

    else:
        #Comprobamos que se ha pasado un OID
        if oid:
            try:
                
                #Obtengo el valor que ha introducido el usuario y elimino la ventana
                ventana.destroy()
                oid = oid.rstrip('.0')
                #Realizo peticion y obtengo los valores
                if (bool(re.search(r'\d',oid))!=True):
                    #si no contiene un numero
                    oid = traducir_direcciones(oid)
                else : 
                    oid += '.0'
                    oid = oid.strip(' ')
                ip = sesion.hostname
                comunidad = sesion.community
                set_response = set(ip, {str(oid): str(valor)},
                                    hlapi.CommunityData(comunidad))
                datos = list(set_response.items())
                oid = datos[0][0]
                valor = datos[0][1]
                    #Actualizamos la etiqueta referente al campo de respuestas para mostrar el resultado de la operacion
                etiquetaRespuesta.config(
                    text="Respuesta de {0}: '{1}'".format(oid, valor))
                lista_parametro.append((oid, valor, sesion.hostname))
                historial(lista_parametro, "SET")
            except:
                    #En caso de excepcion significa que no se ha encontrado el OID solicitado
                etiquetaRespuesta.config(
                text="El OID introducido no se ha encontrado", fg="red3")
        else:
            etiquetaRespuesta.config(text="Tiene que introducir un oid", fg="red")


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
