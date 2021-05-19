#Esta funcion devuelve True si la consola devuelve un error 'Bad operator', y False si no hay ese error
#El parametro recibido puede ser tanto la salida stdout como una lista
def comprobar_error(stdout):
    #Trabajamos sobre la copia porque stdout es efimero
    copia=stdout
    if isinstance(copia,list):
        if copia[0].decode().strip().startswith("Bad operator"):
            return True
    else:
        if copia.decode().strip().startswith("Bad operator"):
            return True
        else:
            return False
