from subprocess import *
import subprocess
import re
import glob
import os
import time
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
def hello_world(filenames):

	temp=filenames.split()
	file_names = []
	inp_files = []
	for i in temp:
		if(re.match('.*\.c$',i)):
			file_names.append(i)
		else:
			inp_files.append(i)

	
	print(file_names)
	l = ["gcc","-g"]
	l.extend(file_names)
	print(l)
	status = subprocess.call(l)
	# print(result.stdout)

	if status != 0 : 
		print("cannot compile and link", file_names) 
		exit(1)


	
	print()

	len_inp_files = len(inp_files)

	if len_inp_files == 0:
		inp_files.append("")

	path_main = './'
	# test_files = sorted(glob.glob(path_main + '/in*.txt'))
	res_files = sorted(glob.glob(path_main + '/out*.txt'))
	# res_files = res_files[:len_inp_files]



	c = 0
	score = []
	for (test, res) in map(lambda x, y : (x, y), inp_files, res_files) :
		outfile = open("zzz"+str(c)+".dat","w")
		outfile.close()
		pid = os.fork()
		if pid:
			time.sleep(0.1)
			os.kill(pid, 16)
			(pid, x) = os.wait()
			#print(x)
			signal = x & 0xff
			status = x >> 8
			#print(status, signal)
		else:
			print(test, res)
			os.execvp("./a.out", (test, "zzz"+str(c)+".dat"))
#		if status != 0 and signal != 0:
		if status != 0:
			print("cannot run : ", name, file = outfile)
			
		else:
			print("----")
			os.system("cat ./zzz.dat")
			print("----")
			status = os.system("cmp -s " + "zzz"+str(c)+".dat " + res)
			if status == 0 :
				print("ok")
				score.append(10)
			else:
				print("not ok")
				score.append(0)
		c+=1

	s = ""
	for i in range(len(score)):
		s+="For Test Case "+inp_files[i]+": "+str(score[i])+" marks\n"
	s+= "\nYour Total Score is "+str(sum(score))+" marks\n\n"
	for inp in inp_files:
		p = Popen(['gdb', 'a.out'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines = True)
		if(inp == ""):
			p.stdin.write('r\n')
		else:
			print("For test case "+inp+":")
			s+="For test case "+inp+":\n"
			file_reader = open(inp,'r')
			for i in file_reader.readlines():
				s+= i
			file_reader.close()
			s+="\nYour Output:\n\n"
			file_reader = open("zzz"+str(inp_files.index(inp))+".dat",'r')
			for i in file_reader.readlines():
				s+= i
			file_reader.close()
			s+="\nExpected Output:\n\n"
			file_reader = open(res_files[inp_files.index(inp)],'r')
			for i in file_reader.readlines():
				s+= i
			file_reader.close()
			p.stdin.write('r <'+inp+'\n')
		p.stdin.write('info locals\n')
		p.stdin.write('bt\n')
		out , errors = p.communicate()
		glob_list = out.split('\n')
		# print(glob_list)
		c = 0
		for i in glob_list:
			if i.startswith('(gdb)') and c == 0:
				c +=1
			elif i.startswith('(gdb)') and (c == 1 or c == 2):	
				print("\n")
				s+="\n"
				print(i[6:])
				s += i[6:]+"\n"
				c+=1
			elif i.startswith('(gdb)') and c == 3:	break
			elif (c == 1 or c == 2 or c == 3):	
				print(i)
				s += i+"\n"
		print()
		s += "\n\n"
	return s
	
# print(hello_world())























# out = a.communicate()


# command = "./a.out < in03.txt"

# result = run(command, universal_newlines=True,shell = True, text = True)
# print(result.returncode, result.stdout, result.stderr)

# command = "./a.out < in03.txt "
# subprocess.call([command],shell = True)