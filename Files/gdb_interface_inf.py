from subprocess import *
import subprocess
import os
import time
import signal
import sys

outfile = open("out.txt", "a")

file_names = input('Enter C Program Names : ')

l = ["gcc","-g"]
l.extend(file_names.split())
status = subprocess.call(l)

if status != 0 : 
	print("cannot compile and link", file_names) 
	exit(1)


inp_files = input("Enter input as a text file:")
print()
inp_files = inp_files.split()
if len(inp_files) == 0:
	inp_files.append("")

non_inf_files = []
# print(inp_files)
for inp in inp_files:
	pid = os.fork()
	if pid:

		time.sleep(0.1)
		temp_pid = subprocess.call(['pidof a.out'],shell = True)
		print(type(temp_pid))
		os.kill(pid, signal.SIGSEGV)	
		(pid, x) = os.wait()
		if x==0:
			non_inf_files.append(inp)
		# print("x: ",x)
	else:
		# print(inp)
		command = "./a.out"+" < "+inp
		subprocess.call([command],shell = True,stdout=subprocess.DEVNULL)
		sys.exit(0)	

for inp in inp_files:
	print("for test case "+inp)
	if inp in non_inf_files:
		glob_list = []
		p = Popen(['gdb', 'a.out'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, \
		stderr=subprocess.PIPE,universal_newlines = True, text = True)

		p.stdin.write('r <'+inp+'\n')
		p.stdin.write('info locals')
		out , errors = p.communicate()
		glob_list = out.split('\n')

		c = 0
		for i in glob_list:
			if i.startswith('(gdb)') and c == 0:
				c +=1
			elif i.startswith('(gdb)') and c == 1:	
				print("\n")
				print(i[6:])
				c+=1
			elif i.startswith('(gdb)') and c == 2:	break
			elif c == 1:	print(i)
			elif c == 2:	print(i)
		print()
	else:
		print("Code ran into infinite loop !!")

# for inp in inp_files:
# 	print("for test case "+inp)
# 	glob_list = []
# 	p = Popen(['gdb', 'a.out'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines = True)
# 	if inp in non_inf_files:
# 		p.stdin.write('r <'+inp+'\n')
# 		p.stdin.write('info locals')
# 		out , errors = p.communicate()
# 		glob_list = out.split('\n')

# 		c = 0
# 		for i in glob_list:
# 			if i.startswith('(gdb)') and c == 0:
# 				c +=1
# 			elif i.startswith('(gdb)') and c == 1:	
# 				print("\n")
# 				print(i[6:])
# 				c+=1
# 			elif i.startswith('(gdb)') and c == 2:	break
# 			elif c == 1:	print(i)
# 			elif c == 2:	print(i)
# 		print()
# 	else:
# 		print("code ran into -- infinite loop !!")
# 		pid = os.fork()
# 		if pid:
# 			time.sleep(0.1)
# 			os.kill(pid, signal.SIGINT)	
# 			(pid, x) = os.wait()
# 		else:
# 			p.stdin.write('r <'+inp+'\n')
# 			sys.exit(0)
# 		p.stdin.write('info locals')
# 		pid = os.fork()
# 		if pid:
# 			time.sleep(0.1)
# 			os.kill(pid, signal.SIGINT)	
# 			(pid, x) = os.wait()
# 		else:
# 			out , errors = p.communicate()	
# 			sys.exit(0)
# 		print("hello")	
# 		# os.kill(p.pid, signal.SIGQUIT)
# 		# p.stdin.write('r <'+inp+'\n')
# 		# p.terminate()
# 		# out , errors = p.communicate()
# 		# out = p.stderr
# 		# print(out)





















# out = a.communicate()


# command = "./a.out < in03.txt"

# result = run(command, universal_newlines=True,shell = True, text = True)
# print(result.returncode, result.stdout, result.stderr)

# command = "./a.out < in03.txt "
# subprocess.call([command],shell = True)
