#-*-coding: utf-8-*-
from sys import argv 
from os import chdir, getcwd, listdir, system, path
from platform import python_version as pv
from platform import platform
from threading import *
class Searcher():
	def __init__(self):
		self.od = getcwd() #od = Original directory
	def find(self,d,f ,rt = "none"):
		chdir(d)
		files = listdir()
		fobjs = [getcwd()]
		for file in files:
			if rt == "none":
				if file == f:
					return True
			else:
				if rt == "getdirs":
					if path.isdir(file):
						fobjs.append("{}\\{}".format(getcwd(),file))
				elif rt == "getfiles":
					if path.isfile(file):
						fobjs.append(file)
	def low(self, f):
		if self.find(getcwd(), f):
			print("File '{}' found in {}".format(f, getcwd()))
		else:
			print("File '{}' not found".format(f))
	def nth(self, f):
		dirs = self.find("none", "getdirs")
		for d in dirs:
			self.find("{}\\{}".format(getcwd(), d) ,f)
	def gointo(self, d, f):
		rtd = []
		for file in listdir(d):
			if path.isdir(file):
				rtd.append(file)
			else:
				if file == f:
					return (d, True)
		return rtd
	def h(self, f):
	    dirs = self.find(getcwd(), "none", "getdirs")
	    while True:
	    	c = self.dirlist(dirs)
	    	if c[1] == True:
	    		print("File '{}' found in {}".format(f, c[0]))
	    		break
	    	else:
	    		dirs = c
	def dirlist(self, lst):
	    for d in lst:
	    	comp = self.gointo(d, f)
	    	if comp[1] == True: 	
	    		return comp	
	    return comp

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
					for file in listdir():
						if path.isdir(file):
							print("[dir] {}".format(file))
						else:
							print(file)
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
	file = ""
	cat = ""
	ogs = True
	for arg in argv:
		if arg [0] != "-":
			count+=1
			continue
		if arg=="-console":
			print("Starting Console")
			ogs = False
			break
		elif arg == "-file":
			print("File declared")
			file = argv[count +1]
		elif arg == "-m":
			print("Mode declared")
			cat = argv[count + 1]
		else:
			print("[Error] arg '{}' not found".format(arg))
			exit()
		count += 1
	if ogs == True:
		if cat == "h":
			main.h(file)
		elif cat == "nth":
			main.nth(file)
		elif cat == "low":
			main.low(file)
		else:
			print("[Error] '{}' mode not found".format(cat))
	else:
		main.console()