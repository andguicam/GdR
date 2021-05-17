from puresnmp import table
from datetime import timedelta


def tabla_a_lista(IP,COMMUNITY,OID,l_final):

    result = table(IP, COMMUNITY, OID)
    l_aux=[]
    l_aux_copia=[]

    for linea in result:
        linea = linea.values()
        for elemento in linea:
            if isinstance(elemento,int) or str(elemento).isdigit() or isinstance(elemento,float):
                #Ya esta limpio, simplemente añadimos a la lista auxiliar
                l_aux.append(elemento)
            else:
                #Es una cadena de bytes que tenemos que limpiar antes de añadir
                if isinstance(elemento,timedelta):
                    #si es un timedelta lo metemos como segundos
                    l_aux.append(elemento.total_seconds())
                else:
                    if isinstance(elemento,str):
                        elemento_limpio = elemento.strip("\\x00")
                        l_aux.append(elemento_limpio)
                    else:
                        if len(elemento)==4:
                            #es una direccion ip
                            l_aux.append('.'.join(f'{c}' for c in elemento))
                        else:
                            #es un byte array
                            try:
                                elemento_limpio = elemento.decode().strip("\x00")
                                l_aux.append(elemento_limpio)
                            except:
                                #Si salta la excepcion tenemos que meterlo en la lista como valor haxadecimal (que es lo que es)
                                l_aux.append(elemento.hex())
        l_aux_copia=l_aux.copy()
        l_final.append(l_aux_copia)
        l_aux.clear()
    return l_final