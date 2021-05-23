#Esta funcion devuelve True si la consola devuelve un error 'Bad operator', y False si no hay ese error
#El parametro recibido puede ser tanto la salida stdout como una lista
def comprobar_error(stdout):
    #Trabajamos sobre la copia porque stdout es efimero
    copia=stdout
    if isinstance(copia,list):
        if isinstance(copia[0],str):
            #Es una lista de strings
            if copia[0].startswith("Bad operator"):
                return True
            else:
                return False
        else:
            #Es la lista, debemos usar decode
            if copia[0].decode().strip().startswith("Bad operator"):
                return True
            else:
                return False
    else:
        if copia.decode().strip().startswith("Bad operator"):
            return True
        else:
            return False
