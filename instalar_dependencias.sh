#!/bin/sh
sudo apt update
sudo apt install libsnmp-dev snmp-mibs-downloader gcc python-dev  snmp python3 python3-pip python3-tk -y
pip3 install puresnmp easysnmp pysnmp
echo "---------------------------------------------------"
echo "INSTALACION DE DEPENDENCIAS COMPLETADA."
echo "Por favor ejecute el fichero interfaz_inicio.py para ejecutar el programa."
echo "Ejemplo de ejecucion: $ python3 interfaz_inicio.py"
echo "---------------------------------------------------"
