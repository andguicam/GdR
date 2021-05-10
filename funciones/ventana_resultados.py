from tkinter import *
from tkinter import ttk
def ventana_resultados(lista):
    ventana=Tk()
    ventana.title("Respuesta de la operación")
    ventana.geometry("600x200")

    main_frame=Frame(ventana)
    main_frame.pack(fill=BOTH,expand=1)
    
    canvas=Canvas(main_frame)
    canvas.pack(side=LEFT,fill=BOTH,expand=1)
    scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)

    canvas.configure(yscrollcommand=scrollbar)
    canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox("all")))

    second_frame= Frame(canvas)

    canvas.create_window((0,0),window=second_frame,anchor="nw")

    #creamos etiquetas e imprimimos las respuestas
    i=0 #Contador para las filas
    for elemento in lista:
        oid=elemento[0]
        valor=elemento[1]
        ip=elemento[2]
        if valor=="Error en la petición":
            Label(second_frame,text="Respuesta de {0}: Error en la petición".format(ip),bg="red3").grid(row=i,column=0,padx=10)
            i+=1
        else:
            Label(second_frame,text="Respuesta de {0}: {1}: '{2}'".format(ip,oid,valor),bg="SpringGreen2").grid(row=i,column=0,padx=10)
            i+=1
