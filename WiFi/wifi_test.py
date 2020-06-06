import pywifi 
from pywifi const 



def gic():
	wifi=pywifi.PyWiFi()
	

	ifaces=wifi.interfaces()[0]
	print(wifi)
	print(ifaces.name())


	gic()
	pass