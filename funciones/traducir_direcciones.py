import subprocess
from sys import stderr
def convertir (lineas):
    l=[] #Contiene la linea con todos los titulos de la tabla
    l_limpia=[]
 #le tenemos que eliminar el parametro salto de linea
    for el in lineas:
        l.append(el.decode())
 
        res=" ".join(l[0].split())
  

    l_limpia.append(res.split(" "))
   
    #convertimos la lista en string
    str_limpia = ''.join(map(str, l_limpia))
   
    #eliminamos los elementos inecesarios
    str_limpia_f = str_limpia.translate({ord(i):None for i in "['"})
    str_limpia_ff =str_limpia_f.translate({ord(i):None for i in "']"})
    return str_limpia_ff

def traducir_direcciones (oid):
    #al ser un oid de letras le tenemos que añadir la direccion completa
    #añadimos el .0 al oid
    oid =oid +".0"
    #llamamos al proceso que nos devuelve la informacion que tenemos  
    #que enviar al otro proceso para que nos traduzca el oid
    out = subprocess.Popen(['snmptranslate','-IR',oid], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr =out.communicate()
  
    #tenemos que eliminar todos los elements que no nos hacen falta
    lineas=stdout.splitlines()
    str_limpia_ff = convertir(lineas)
    #este proceso nos devulve el oid numerico
    out_f = subprocess.Popen(['snmptranslate','-On',str_limpia_ff], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout_f,stderr_f=out_f.communicate()
    #eliminamos todos los elementos que no nos hagan falta
    lineas =stdout_f.splitlines()
    str_oid = convertir(lineas)
   
    #devolvemos el oid numerico
    return str_oid

def presentar_direcciones(oid, campo_respuesta):
    #traducir el oid de no numerico a numerico
    str_oid = traducir_direcciones(oid)
    campo_respuesta.config(text=str_oid, fg ="green3")
   