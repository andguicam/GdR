from funciones.comprobar_error import comprobar_error
import subprocess
from sys import stderr
from funciones.comprobar_version import comprobar_version
from funciones.comprobar_error import comprobar_error

#TODO:Revisar esta funcion
def convertir(lineas):
    l = []  # Contiene la linea con todos los titulos de la tabla
    l_limpia = []
 #le tenemos que eliminar el parametro salto de linea
    for el in lineas:
        if not el.decode().startswith("Bad operator"):
            #Si hay error no queremos que esa linea se añada a la lista,
            #luego no entrara en el if
            l.append(el.decode()) #No se muy bien que pinta aqui l. ¿Sobra?
            res = " ".join(el.decode().split())

    l_limpia.append(res.split(" "))

    #convertimos la lista en string
    str_limpia = ''.join(map(str, l_limpia))

    #eliminamos los elementos inecesarios
    str_limpia_f = str_limpia.translate({ord(i): None for i in "['"})
    str_limpia_ff = str_limpia_f.translate({ord(i): None for i in "']"})
    return str_limpia_ff


def traducir_direcciones(oid):
    #quitamos el .0 en caso de que venga en lo que introduce el usuario
    oid=oid.rstrip(".0")
        
    #al ser un oid de letras le tenemos que añadir la direccion completa
    #añadimos el .0 al oid
    oid = oid + ".0"
    #llamamos al proceso que nos devuelve la informacion que tenemos
    #que enviar al otro proceso para que nos traduzca el oid
    if comprobar_version()=='5.9': #5.9 es la version de MacOS
        out = subprocess.Popen(['snmptranslate', '-IR', oid],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        lineas = stdout.splitlines()
        str_limpia_ff = convertir(lineas)
        out_f = subprocess.Popen(['snmptranslate', '-On', str_limpia_ff],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout_f, stderr_f = out_f.communicate()
        lineas = stdout_f.splitlines()
        str_oid = convertir(lineas)
    else:
        try:
            out=subprocess.check_output('snmptranslate '+str(oid)+' -IR -On -m ALL', stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError:
            return False

        lineas = out.decode().strip().splitlines()

        if comprobar_error(lineas):
            #Tiene error, cogemos la segunda linea como valor del oid
                str_oid = lineas[1].replace('[', '').replace(']', '')
        else:
            #No tiene error, la primera linea es el oid
            str_oid=lineas[0].replace('[','').replace(']','')


   
    return str_oid


def presentar_direcciones(oid, campo_respuesta):
    #type(oid)=str siempre se cumple. aqui hay que comprobar lo que reyes está desarrollando
    if(oid==" "): #or type(oid)==str):
        campo_respuesta.config(text="Introduce un oid no numerico", fg="red")
    #traducir el oid de no numerico a numerico
    else:
        str_oid = traducir_direcciones(oid)
        if str_oid==False:
            #No existe el oid introducido, lo indicamos
            campo_respuesta.config(text="No existe el oid introducido.", fg="red")
        else:
            campo_respuesta.config(text=str_oid, fg="green3")
