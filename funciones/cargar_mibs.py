from easysnmp import Session

def system_mib():
	#Rellenamos un diccionario con los valores que queremos de system mib
	system_mib = ["sysDescr", "sysObjectID",  "sysUpTime", "sysContact", "sysName", "sysLocation","sysORTable"]
	return system_mib