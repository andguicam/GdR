import subprocess

def comprobar_version():
    version = subprocess.Popen(['snmptable', '-V'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)

    copia = version.communicate()
    if copia[0].decode().strip().split()[-1] == '5.9':
        return '5.9'
    else:
        return 'Otra version'