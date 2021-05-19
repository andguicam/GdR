import easysnmp
from funciones.leer_agentes import leer_agentes
from funciones.ventana_resultados import ventana_resultados
from easysnmp import Session 
from funciones.escribir_agentes import escribir_agentes
from funciones.historial import historial
#Recibe como parámetro la sesión y el OID (y la ventana), y actualiza la ventana con la respuesta
def get_handler(sesion,oid,etiquetaRespuesta,estado_checkbox,estado_checkbox_exportar):
    lista_parametro=[]
    if estado_checkbox.get():
        #hay que hacer varias peticiones. Los resultados se devolverán en una lista (de tuplas)
        lista=[]
        agentes=leer_agentes()
        for agente in agentes:
            ip=agente[0]
            comunidad=agente[1] #Para eliminar el \n final en caso de que lo haya
            lista.append(peticion_get_checkbox(ip,comunidad,oid))
        #imprimimos los resultados en una ventana aparte
        ventana_resultados(lista,"GET") #Ventana resultados ya imprime la impresion en el archivo de log
        if estado_checkbox_exportar.get():
            escribir_agentes(lista, oid)

    else:
        print (type(oid))
        #Comprobamos que se ha pasado un OID
        if oid:
            try:
                #añadimos el .0 directamente, podemos incluir valores no numericos
                #Realizo peticion y obtengo los valores
                oid = oid.rstrip('.0')
                get_response = sesion.get((oid, '0'))
                oid=get_response.oid
                valor=get_response.value
                #Actualizamos la etiqueta referente al campo de respuestas para mostrar el resultado de la operacion
                etiquetaRespuesta.config(text="Respuesta de {0}: '{1}'".format(oid,valor),fg="SpringGreen2")
                lista_parametro.append((oid, valor, sesion.hostname))
                historial(lista_parametro,"GET")
            except:
                #En caso de excepcion significa que no se ha encontrado el OID solicitado
                etiquetaRespuesta.config(text="El OID introducido no se ha encontrado", fg="red3")
        
        else:
            etiquetaRespuesta.config(text="Tiene que introducir un oid", fg="red")

def peticion_get_checkbox(ip,comunidad,oid):
    try:
        sesion = Session(hostname=ip, community=comunidad, version=2)
        get_response_checkbox=sesion.get(oid)
        return(get_response_checkbox.oid,get_response_checkbox.value,ip)
    except:
        return (oid,"Error en la petición",ip)


