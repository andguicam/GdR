import subprocess

def snmptable(ip,comunidad,oid):
    linea=3 #Linea donde estan los indices de la tabla
    l=[] #Contiene la linea con todos los titulos de la tabla
    l_limpia=[] #Contiene en la primera posicion la linea con los titulos de las columnas
                #Es lo que queremos devolver


    out = subprocess.Popen(['snmptable','-v','1','-c', comunidad, ip, oid],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

    stdout,stderr=out.communicate()
    lineas=stdout.splitlines()
    for el in lineas:
        l.append(el.decode())
    try:
        res=" ".join(l[2].split())
    except:
        #Si tenemos una excepcion es porque no existe tabla para el OID introducido
        return "OID invalido. No hay tabla asociada"

    l_limpia.append(res.split(" "))

    return l_limpia



