from os import error
from funciones.comprobar_version import comprobar_version
import subprocess
from funciones.comprobar_version import comprobar_version
from funciones.comprobar_error import comprobar_error


def snmptable(ip,comunidad,oid):
    linea=3 #Linea donde estan los indices de la tabla
    l=[] #Contiene la linea con todos los titulos de la tabla
    l_limpia=[] #Contiene en la primera posicion la linea con los titulos de las columnas
                #Es lo que queremos devolver

    #Necesitamos comprobar la version porque en MacOS se proporciona la version 5.9 de snmptable,
    #que tiene una sintaxis distinta a la version 5.8 que es la que se proporciona en Linux (Ubuntu 20.04)

    version = subprocess.Popen(['snmptable','-V'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    
    copia=version.communicate()
    if comprobar_version() == '5.9':
        out = subprocess.Popen(['snmptable','-v', '1', '-c', comunidad, ip, oid],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
        
    else:
        out = subprocess.Popen(['snmptable',ip,oid,'-c',comunidad,'-v','1','-O','a','-m','ALL'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)


    stdout,stderr=out.communicate()
    lineas=stdout.splitlines()
    for el in lineas:
        l.append(el.decode())
    try:
        if comprobar_error(stdout):
            res=" ".join(l[3].split())
        else:
            res = " ".join(l[2].split())
    except:
        #Si tenemos una excepcion es porque no existe tabla para el OID introducido
        return "OID invalido. No hay tabla asociada"

    l_limpia.append(res.split(" "))

    return l_limpia



