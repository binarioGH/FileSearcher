'''#-*-coding: utf-8-*-
from sys import argv
from os import chdir, getcwd, listdir, system
from platform import python_version as pv
from platform import platform
from threading import *

class Searcher():
	def __init__(self):
		self.od = getcwd() #od = Original directory
	def find(self, f ,rt = "none"):
		files = listdir()
		dirs = []
		for file in files:
			if file == isdir: #tengo que buscar como ver si esto es un dir o no en python.
				
		    else:
		    	if file == f:
		    		if rt == "none":
		    			print("''{}'' found in {}".format(f))
	def low(self, f):
		find()
	def nth(self, f):
		pass
	def h(self, f):
		pass
	def search(self, f, category="l"):
		if category == "l":
			t = self.low
		elif category == "n":
			t = self.nth(d)
		elif category == "h":
			t = self.h(d)
		search = Thread(target=target, args=(f,))
		search.daemon = True
		search.start()

		
	def console(self):
		if str(pv())[0] == "3":
			raw_input = input
		if str(platform())[0].lower() == "w":
			clear = "cls"
		else:
			clear = "clear"
		cmd = ""
		while cmd != "exit":
			cmd = raw_input(">>")
			try:
				if cmd == clear:
					system(clear)
				elif cmd[:2] == "cd":
					chdir(cmd[3:])
				elif cmd == "dir":
					for file in 
				elif cmd[:9] == "lowsearch":
					search(cmd[10:], "l")
				elif cmd[:12] == "middlesearch":
					search(cmd[13:], "n")
				elif cmd[:10] == "hardsearch":
					search(cmd[11:], "h")
				elif cmd[:4] == "find":
					search(cmd[5:])
				else:
					print("Command ''{}'' not found.".format(cmd))
			except Exception as e:
				print(e)


if __name__ == '__main__':
	main = Searcher()
	count = 0
	for arg in argv:
		if argv[0] != "-":
			count+=1
			continue
		elif argv=="-console":
			main.console()
			break


'''