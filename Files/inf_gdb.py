from multiprocessing import Process
from subprocess import *
import subprocess
import os
import time
import sys


def debuger(filename, inpfile):

	p1 = Process(target = inf, args = (filename, inpfile))
	p2 = Process(target = gdb)

	p1.start()
	time.sleep(0.5)
	p2.start()

	p1.join()
	p2.join()


def inf(filename, inpfile):

	status = os.system("gcc " + filename + " " +  "main.c " + "-lm " + " 2>/dev/null")
	#os.system("./a.out <" + inpfile )
	subprocess.run(['./a.out', '<', 'inpfile'], stdout=subprocess.PIPE)


def gdb():

	# p = Popen(['pidof', 'a.out'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, \
	# 	stderr=subprocess.PIPE,universal_newlines = True, text = True)
	# out , errors = p.communicate()



	result = subprocess.run(['pidof', 'a.out'], universal_newlines=True,shell = True, text = True)
	#result = subprocess.call(['pidof a.out'], shell = True)
	
	subprocess.call(['kill', result.stdout], shell = True, text = True)
	print(result.stdout)




if __name__ == "__main__" :

	filename = input("enter filename: ")
	inpfile = input("enter input file: ")
	debuger(filename, inpfile)
