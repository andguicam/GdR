from funciones.snmptable import snmptable
from funciones.tabla_a_lista import tabla_a_lista
import tkinter
from tkinter import ttk

def get_tree(session, oid):

    ip = session.hostname
    comunidad = session.community
    res = snmptable(ip, comunidad, oid)
    lista = []

    if res == "OID invalido. No hay tabla asociada":
        print("No hay tabla asociada a ese OID")
        lista = None 
    else:
        #La tabla existe y seguimos con el proceso
        lista = tabla_a_lista(ip, comunidad, oid, res)
        
    return lista


