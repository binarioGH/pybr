#-*-coding: utf-8-*-
from sys import argv
from os import system, getcwd
def interactiveinterpreter():
	print("PYBR es un lenguaje de programación que continúa en desarrollo.")
	cmm = ""
	commands = {"cls":"cls()", "pwd": "pwd()"}
	while cmm != "exit":
		cmm = input(">>>>")
		if cmm in commands:
			cmm = commands[cmm]
		try:
		    if cmm[:11] == "interpreter":
		    	continue

		except:
			pass
		try:
			exec(cmm)
		except Exception as e:
			print(e)
	exit()
def cls():
	system("cls")
def pwd():
	print(getcwd())

def interpreter(file):
	try:
		f = open(file, "r")
	except Exception as e:
		print(e)
		exit()
	c = False
	code = f.readlines()

	f.close()
	for l in code:
		l = l.strip("\n")
		if l.strip(" ") == "startcmd".strip(""):
			c = True
			continue
		elif c == True:
			if l.strip(" ") != "endcmd".strip(" "):
				system(l)
			else:
				c = False 
		else:
			exec(l)



if __name__ == '__main__':
	if len(argv) == 1:
		interactiveinterpreter()
	else:
		interpreter(argv[1])