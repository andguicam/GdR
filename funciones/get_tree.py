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
    else:
        #La tabla existe y seguimos con el proceso
        lista = tabla_a_lista(ip, comunidad, oid, res)
        
        return tree_generator(lista)

def tree_generator(lista):

    #Aqui no he añadido ninguna scrollbar ni asociado a ventana ni nada, esto
    #se puede tocar sin problemas para que devuelva el arbol como sea necesario
    
    tree = ttk.Treeview()

    #-------------Generacion del arbol------------------
    #Definir columnas
    tree['column'] = lista[0]

    #Formateo columnas
    tree['show'] = 'headings'

    for titulo in lista[0]:
        tree.heading(titulo, text=titulo)

    i = 0  # nos servira para saltarnos la primera fila, que es donde estan los titulos
    for fila in lista:
        if i != 0:
            tree.insert("", "end", values=fila)
        i += 1
    #-------------Fin generacion del arbol---------------
    return tree

