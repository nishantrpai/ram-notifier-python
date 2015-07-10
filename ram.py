import pynotify
import psutil
from time import sleep
def sendmessage():
	pynotify.init("Test")
	message = str(psutil.phymem_usage())
	mes = ''	
	for m in message : 
		if m == ',' or m == ')' or m == '(':
			mes += '\n'
		elif m == "=":
			mes += ':'
		elif m == "L" or m == "l":
			mes += "bytes"	
		else:
			mes += m

	notice = pynotify.Notification("RAM SIZE",mes)
	notice.show()
	return
	
while True:
	sendmessage()
	sleep(60*60)

