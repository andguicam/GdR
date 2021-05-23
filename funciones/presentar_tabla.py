from tkinter import *
import re
from tkinter.ttk import Treeview
from funciones.get_tree import get_tree
from funciones.limpiar import *
from funciones.exportar_tabla import exportar_tabla
from funciones.traducir_direcciones import traducir_direcciones

def presentar_tabla(session, oid, app,campo_respuesta,estado_checkbox_exportar):
    #limpiamos el campo de respuesta
    limpiar_campo(campo_respuesta)
    #traducimos a oid numerico si se ha introducido el nombre
    oid = oid.rstrip('.0')
    if (bool(re.search(r'\d',oid))!=True):
        #si no contiene un numero
        oid = traducir_direcciones(oid)
    #volvemos a quitar el .0 que se le añade en traducir oid
    oid = oid.rstrip('.0')
    #obtenemos la lista 
    lista = get_tree(session, oid)
    if (lista ==None):
        campo_respuesta.config(text="El oid introducido no es una tabla", fg='red3')
    else:
        #definimos la scroll bar 
        respuesta_frame=Frame(app)
        respuesta_frame.configure(bg='snow')
        respuesta_frame.pack(side=BOTTOM)
        scroll_x=Scrollbar(respuesta_frame, orient=HORIZONTAL )
        tree = Treeview(respuesta_frame, xscrollcommand=scroll_x.set)
        scroll_x.config(command=tree.xview)   

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
        tree.pack(expand=True,fill='both')
        scroll_x.pack(side=BOTTOM,fill=X)
        #si esta marcada la casilla exportamos la lista
        if estado_checkbox_exportar.get():
            exportar_tabla(lista, oid)

        #creamos un boton para borrar el frame
        button_limpiar = Button(respuesta_frame, text="Limpiar tabla", bg='snow',command = lambda: limpiar_frame(respuesta_frame))
        button_limpiar.pack(side=TOP)


   
    
   
    
