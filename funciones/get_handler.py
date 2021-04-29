import easysnmp


#Recibe como parámetro la sesión

def get_handler(sesion,campoTexto,etiqueta):

    oid_proporcionado=campoTexto.get()
    if oid_proporcionado:
        try:
            get_response = sesion.get(campoTexto.get())
            oid=get_response.oid
            valor=get_response.value
            etiqueta.config(text="Respuesta de {0}: '{1}'".format(oid,valor),bg="SpringGreen2")
        except:
            etiqueta.config(text="El OID introducido no se ha encontrado", bg="red3")
    else:
        print("Tienes que introducir un OID")