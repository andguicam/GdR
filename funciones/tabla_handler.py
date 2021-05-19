from funciones.presentar_tabla import presentar_tabla
from funciones.snmptable import snmptable
from funciones.tabla_a_lista import tabla_a_lista
from funciones.historial import historial
from funciones.exportar_tabla import exportar_tabla
from funciones.presentar_tabla import presentar_tabla
def tabla_handler(session,oid,campo_respuesta,estado_checkbox_exportar):
    ip=session.hostname
    comunidad=session.community
    res=snmptable(ip, comunidad, oid)
    lista=[] #Lista con todos los elementos

    lista_parametro=[] #Para registrar en logs
    tipo_peticion='TABLA'

    if res == "OID invalido. No hay tabla asociada":
        #La tabla no existe. Informamos de ello
        campo_respuesta.config(text="El OID introducido no es una tabla", fg="red3")
        #Registramos en el historial
        lista_parametro.append((oid, "con errores", ip))
        historial(lista_parametro, tipo_peticion)
    else:
        campo_respuesta.config(
            text="Exito en la operacion.", fg="SpringGreen2")
        #La tabla existe y seguimos con el proceso
        lista=tabla_a_lista(ip, comunidad, oid, res)
        #Registramos en el historial
        lista_parametro.append((oid, "sin errores", ip))
        historial(lista_parametro, tipo_peticion)
        #Informamos del exito en la operacion por el campo de respuesta
        if estado_checkbox_exportar.get():
            #Si esta marcado exportamos la tabla en formato csv
            exportar_tabla(lista, oid)
        #Representamos la tabla en la ventana
        presentar_tabla(campo_respuesta, lista, oid)
       
