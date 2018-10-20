#-*-coding: utf-8-*-
from sys import argv
from os import system, getcwd
def interactiveinterpreter():
	print("PYBR es un lenguaje de programación que continúa en desarrollo.")
	cmd = ""
	commands = {"cls":"cls()", "pwd": "pwd()"}
	while cmd != "exit":
		cmd = input(">>>>")
		if cmd in commands:
			cmd = commands[cmd]
		try:
		    if cmd[:11] == "interpreter":
		    	continue

		except:
			pass
		try:
			exec(cmd)
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
	for l in f:
		exec(l)


if __name__ == '__main__':
	if len(argv) == 1:
		interactiveinterpreter()
	else:
		interpreter(argv[1])



