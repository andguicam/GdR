from tkinter import *
from tkinter import ttk
def ventana_tablas(lista):
    ventana = Tk()
    ventana.title("Visor")
    ventana.geometry("600x235")

    treeframe=Frame(ventana)
    treeframe.pack(fill='both')
    #tree_scrolly=Scrollbar(treeframe,orient='vertical')
    tree_scrollx = Scrollbar(treeframe, orient='horizontal')

    #TODO: las dos barras de scroll, o si con las flechas/rueda del raton ya es suficiente
    #tree = ttk.Treeview(treeframe,yscrollcommand=tree_scrolly.set,xscrollcommand=tree_scrollx.set)
    tree = ttk.Treeview(treeframe, xscrollcommand=tree_scrollx.set)
    
    #tree_scrolly.config(command=tree.yview)
    tree_scrollx.config(command=tree.xview)
    
    #Definir columnas
    tree['column'] = lista[0]

    #Formateo columnas
    tree['show'] = 'headings'
    
    for titulo in lista[0]:
        tree.heading(titulo,text=titulo)
    
    i=0 #nos servira para saltarnos la primera fila, que es donde estan los titulos
    for fila in lista:
        if i!=0:
            tree.insert("", "end",values=fila)
        i+=1

    tree.pack(expand=True,fill='both')
    #tree_scrolly.pack(side=RIGHT, fill=Y)
    tree_scrollx.pack(side=BOTTOM, fill=X)


    ventana.mainloop()
