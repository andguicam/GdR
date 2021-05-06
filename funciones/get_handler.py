import easysnmp
from funciones.leer_agentes import leer_agentes
from funciones.ventana_resultados import ventana_resultados
from easysnmp import Session 

#Recibe como parámetro la sesión y el OID (y la ventana), y actualiza la ventana con la respuesta
def get_handler(sesion,oid,etiquetaRespuesta,estado_checkbox):

    if estado_checkbox.get():
        #hay que hacer varias peticiones. Los resultados se devolverán en una lista (de tuplas)
        lista=[]
        agentes=leer_agentes()
        for agente in agentes:
            ip=agente[0]
            comunidad=agente[1]
            lista.append(peticion_get_checkbox(ip,comunidad,oid))
        #imprimimos los resultados en una ventana aparte
        ventana_resultados(lista,ip)

    else:
        #Comprobamos que se ha pasado un OID
        if oid:
            try:
                #Realizo peticion y obtengo los valores
                get_response = sesion.get(oid)
                oid=get_response.oid
                valor=get_response.value
                #Actualizamos la etiqueta referente al campo de respuestas para mostrar el resultado de la operacion
                etiquetaRespuesta.config(text="Respuesta de {0}: '{1}'".format(oid,valor),bg="SpringGreen2")
            except:
                #En caso de excepcion significa que no se ha encontrado el OID solicitado
                etiquetaRespuesta.config(text="El OID introducido no se ha encontrado", bg="red3")
        else:
            print("Tienes que introducir un OID")

def peticion_get_checkbox(ip,comunidad,oid):
    try:
        sesion = Session(hostname=ip, community=comunidad, version=2)
        get_response_checkbox=sesion.get(oid)
        return(get_response_checkbox.oid,get_response_checkbox.value)
    except:
        return (oid,"Error en la petición")


