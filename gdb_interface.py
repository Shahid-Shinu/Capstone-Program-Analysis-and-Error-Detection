from subprocess import *
import subprocess
import re
import glob
import os
import time
import signal
import sys
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
def hello_world(filenames):

	temp=filenames.split()
	file_names = []
	inp_files = []
	for i in temp:
		if(re.match('.*(\.c|\.h)$',i)):
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

	non_inf_files = []

	for inp in inp_files:
		pid = os.fork()
		if pid:
			time.sleep(0.1)
			os.kill(pid, signal.SIGSEGV)	
			(pid, x) = os.wait()
			if x==0:
				non_inf_files.append(inp)
			# print("x: ",x)
		else:
			# print(inp)
			command = "./a.out"+" < "+inp
			subprocess.call([command],shell = True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
			sys.exit(0)


	path_main = './'
	# test_files = sorted(glob.glob(path_main + '/in*.txt'))
	res_files = sorted(glob.glob(path_main + '/out0*.txt'))
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
			# signal = x & 0xff
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
			os.system("cat ./zzz"+str(c)+".dat")
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
	s+= str(sum(score)//10)+"/"+str(len(score))+" test cases passed\n"
	for i in range(len(score)):
		s+="For Test Case "+inp_files[i]+": "+str(score[i])+" marks\n"
	s+= "\nYour Total Score is "+str(sum(score))+" marks\n\n"
	for inp in inp_files:
		p = Popen(['gdb', 'a.out'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines = True)
		# p.stdin.write('set args 1')
		if inp in non_inf_files:
			file_reader = open("zzz"+str(inp_files.index(inp))+".dat",'r')
			temp_file_data = file_reader.readlines()
			file_reader.close()
			ind_file = inp_files.index(inp)
			print(f'file_data: {temp_file_data}\n score is: {score[ind_file]}')
			if temp_file_data == [] or score[ind_file]:

				#Handles Segmentation Faults and Correct Output

				p.stdin.write('set $argument = 1\n')
				p.stdin.write('source pygdb.py'+'\n')
				p.stdin.write(inp+'\n')

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
				ind_file = inp_files.index(inp)
				if not score[ind_file]:
					s+="segmentation fault"
				s+="\nExpected Output:\n\n"
				file_reader = open(res_files[inp_files.index(inp)],'r')
				for i in file_reader.readlines():
					s+= i
				file_reader.close()

				out , errors = p.communicate()
				print(errors)
				glob_list = out.split('\n')
				# print(glob_list)
				s+="\nDebugger Message:\n\n"

				c = 0
				for i in glob_list:
					if i.startswith('(gdb) quit'):
						break
					elif i.startswith('(gdb) '):
						c = 1
					elif c == 1:
						print(i)
						s += i+"\n"
			else:
				print("here")
				p.stdin.write('set $argument = 3\n')
				p.stdin.write('source pygdb.py'+'\n')
				p.stdin.write(inp+'\n')
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
				ind_file = inp_files.index(inp)
				s+="\nExpected Output:\n\n"
				file_reader = open(res_files[inp_files.index(inp)],'r')
				for i in file_reader.readlines():
					s+= i
				file_reader.close()

				out , errors = p.communicate()
				print(errors)
				glob_list = out.split('\n')
				c = 0
				l = []
				for i in glob_list:
					if i.startswith('(gdb) quit'):
						break
					elif i.startswith('(gdb) '):
						c = 1
					elif c == 1:
						# print(i)
						l.append(i)

				wrong_ouptut_list = []
				flag = 1
				for i in l:
					if i.startswith('Breakpoint') and flag:
						func_str = i
						flag = 0
						temp_str = ""
					elif flag ==0:
						if i.startswith("res"):
							temp = i.split()[-1]
							if temp == "0":
								wrong_ouptut_list.append(["EMPTY",temp_str])
							else:
								wrong_ouptut_list.append([temp,temp_str])
							c +=1
							flag = 1
						else:
							if re.search('printf',i):
								temp_str = i
				print(wrong_ouptut_list)
				corr_output_list = []
				corr_output_file = open('out'+inp_files[inp_files.index(inp)][2:])
				for i in corr_output_file.readlines():
					# print(i)
					corr_output_list.extend(i.split())
				# print()
				print(corr_output_list)
				temp_ind = 0
				for i in range(len(wrong_ouptut_list)):
					if wrong_ouptut_list[i][0] != corr_output_list[i]:
						temp_ind = i
						wrong_str = wrong_ouptut_list[i][1]
						break
				s+="\nDebugger Message:\n\n"
				# print(f'matches till index:{temp_ind}\nline is:{wrong_str}')
				s+="Wrong Output\n"
				s+=func_str+'\n'
				print(wrong_str)
				s+=wrong_str+'\n'
		else:
			p.stdin.write('set $argument = 2\n')
			p.stdin.write('source pygdb.py'+'\n')
			print("For test case "+inp+":")
			s+="For test case "+inp+":\n"
			file_reader = open(inp,'r')
			for i in file_reader.readlines():
				s+= i
			file_reader.close()
			s+="\nYour Output:\n\n"
			s+="\nInfinite Loop\n"
			s+="\nExpected Output:\n\n"
			file_reader = open(res_files[inp_files.index(inp)],'r')
			for i in file_reader.readlines():
				s+= i
			file_reader.close()

			out , errors = p.communicate()
			glob_list = out.split('\n')
			s+="\nDebugger Message:\n\n"
			c = 0
			for i in glob_list:
				if i.startswith('(gdb) quit'):
					break
				elif i.startswith('(gdb) '):
					c = 1
				elif c == 1:
					print(i)
					s += i+"\n"
	return s
	
# print(hello_world())























# out = a.communicate()


# command = "./a.out < in03.txt"

# result = run(command, universal_newlines=True,shell = True, text = True)
# print(result.returncode, result.stdout, result.stderr)

# command = "./a.out < in03.txt "
# subprocess.call([command],shell = True)