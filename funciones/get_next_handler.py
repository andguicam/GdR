import easysnmp

#Recibe como parámetro la sesión y el OID (y la ventana), y actualiza la ventana con la respuesta

def get_next_handler(sesion,oid,etiquetaRespuesta):

    #Comprobamos que se ha pasado un OID
    if oid:
        try:
            #Realizo peeticion y obtengo los valores
            get_response = sesion.get_next(oid)
            oid=get_response.oid
            valor=get_response.value
            #Actualizamos la etiqueta referente al campo de respuestas para mostrar el resultado de la operacion
            etiquetaRespuesta.config(text="Respuesta de {0}: '{1}'".format(oid,valor),bg="SpringGreen2")
        except:
            #En caso de excepcion significa que no se ha encontrado el OID solicitado
            etiquetaRespuesta.config(text="El OID introducido no se ha encontrado", bg="red3")
    else:
        print("Tienes que introducir un OID")
