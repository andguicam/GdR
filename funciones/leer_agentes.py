def leer_agentes():
    lista=[]
    try:
        f=open("agentes/lista_agentes.txt","r")
        for line in f:
            if line!="\n":   #En caso de que exista una ultima que sea linea vacia
                ip,comunidad=line.split(",")
                lista.append((ip,comunidad))
        return lista
    except:
        print("No se ha encontrado la lista de agentes en la carpeta o no está formateada correctamente.")