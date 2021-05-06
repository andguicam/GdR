

from pysnmp.smi import builder, view, compiler, error
import functools
import operator 
def obtener_mib(mib):
   

    # Create MIB loader/builder
    mibBuilder = builder.MibBuilder()

    print('Setting MIB sources...')
    mibBuilder.addMibSources(builder.DirMibSource('/opt/pysnmp_mibs'))
    print(mibBuilder.getMibSources())
    print('done')

    print('Loading MIB modules...'),
    mibBuilder.loadModules(
            mib
            )
    print('done')

    print('Indexing MIB objects...'),
    mibView = view.MibViewController(mibBuilder)
    print('done')


    print('MIB tree traversal')
    #oid, label, suffix = mibView.getFirstNodeName()
    #obtenemos las mibs que nos interesan de SNMPv2-MIB, es decir todas las que no son tablas de momento
    if (mib == "SNMPv2-MIB"):
        oid, label, suffix = mibView.getNodeName(('sysDescr',))
        print (oid)
        nodeDesc =""
        #vamos guardando en dos tablas, en una el nombre y en otra el oid
        oid_table = []
        desc_table = []
     
        while (nodeDesc != "sysORLastChange"):
            try:
                    modName, nodeDesc, suffix = mibView.getNodeLocation(oid)
                    oid_table.append(oid)
                    desc_table.append(nodeDesc)
                    print('%s::%s == %s' % (modName, nodeDesc, oid))
                    oid, label, suffix = mibView.getNextNodeName(oid)


            except error.NoSuchObjectError:
                    break
  
    return desc_table
#funcion que devuleve el oid segun el nombre
def obtener_oid(desc, mib):
    mibBuilder = builder.MibBuilder()

    print('Setting MIB sources...')
    mibBuilder.addMibSources(builder.DirMibSource('/opt/pysnmp_mibs'))
    print(mibBuilder.getMibSources())
    print('done')

    print('Loading MIB modules...'),
    mibBuilder.loadModules(
           mib
            )
    print('done')
    print('Indexing MIB objects...'),
    mibView = view.MibViewController(mibBuilder)
    print('done')
    oid, label, suffix = mibView.getNodeName((desc,))
    #borramos la informacion que no queremos en la variable
    print(type (oid))
    #convertirmos el oid a string
    oid_f=str(list(oid))
    oid_str = [str(int) for int in oid_f]
    oid_str_f = "".join(oid_str)
    print(type (oid_str_f))
    #borramos los parentesis
    oid_str_f = oid_str_f.lstrip("[")
    #despues quitamosl el parentesis del otro lado
    oid_str_f = oid_str_f.rstrip("]")
    #sustituimos las comas por puntos
    oid_str_f=oid_str_f.replace(", ", ".")
    oid_str_f = oid_str_f + '.0'
    print (oid_str_f)
    return oid_str_f

    
