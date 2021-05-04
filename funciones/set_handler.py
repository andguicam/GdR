import easysnmp
from pysnmp import hlapi

from funciones.quicksnmp import set
#Recibe como parámetro la sesión y el OID (y la ventana), y actualiza la ventana con la respuesta

def set_handler(sesion,oid,valor,etiquetaRespuesta):

    #Comprobamos que se ha pasado un OID
    if oid:
        try:
            #Realizo peticion y obtengo los valores
            ip=sesion.hostname
            comunidad=sesion.community
            set_response= set(ip, {str(oid): str(valor)},
                               hlapi.CommunityData(comunidad))
            datos = list(set_response.items())
            oid = datos[0][0]
            valor = datos[0][1]
            #Actualizamos la etiqueta referente al campo de respuestas para mostrar el resultado de la operacion
            etiquetaRespuesta.config(text="Respuesta de {0}: '{1}'".format(oid,valor),bg="SpringGreen2")
        except:
            #En caso de excepcion significa que no se ha encontrado el OID solicitado
            etiquetaRespuesta.config(text="El OID introducido no se ha encontrado", bg="red3")
    else:
        print("Tienes que introducir un OID")
