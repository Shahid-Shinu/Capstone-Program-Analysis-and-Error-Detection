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

def valgrind_out(list_of_filenames, inp):


	l = ["gcc","-g"]
	l.extend(list_of_filenames)
	status = subprocess.call(l)

	if status != 0 : 
		print("cannot compile and link", file_names) 
		exit(1)
	
	command = f'valgrind --log-file="val_out.txt" --leak-check=full --track-origins=yes  ./a.out < {inp}'
	# print(command)

	subprocess.call([command], shell=True)
	# print(output)


	f = open("val_out.txt")
	res = ''
	flag = 0

	for i in f.readlines():
		if flag:
			res += i
		if re.search('HEAP SUMMARY',i):
			flag = 1
			res += i

	return res


def wrong_output(list_of_filenames,inp,inp_files):
	result = ""
	pSmts = dict()
	for filename in list_of_filenames:

	    command = "grep -n '^\s*printf' "+ filename+" | cut -d : -f 1"
	    output = subprocess.check_output([command],shell = True,universal_newlines = True)

	    if( output != '' ):
	        output = output.split('\n')
	        pSmts[filename] = output[ :-1]
	# print(pSmts)

	for filename in pSmts.keys():

	    file1 = open(filename, 'r')
	    list_of_lines = file1.readlines()
	    file1.close()

	    pCount = 0
	    for lineNo in pSmts[filename]:

	        statement = '{printf("' + filename + ':' + lineNo + '#");\n'

	        list_of_lines.insert(int(lineNo) + pCount-1, statement)
	        statement='printf("#");}\n'
	        list_of_lines.insert(int(lineNo) + pCount+1, statement)
	        pCount += 2

	    filename = 'dummy_'+filename
	    file2 = open(filename, 'w')
	    file2.writelines(list_of_lines)
	    file2.close()

	filenames = list(set(list_of_filenames) - set(pSmts.keys()))
	filenames = ' '.join(filenames)
	filenames = ' dummy_'.join(pSmts.keys()) + ' ' + filenames

	command = "gcc dummy_" + filenames
	subprocess.run([command] ,shell = True)
	command = "script -c './a.out < " + inp + "' -q dummy_output.txt"
	subprocess.run([command],shell = True)
	f1 = open('dummy_output.txt','r')
	output = f1.readlines()
	output = output[1:-2]
	output = ''.join(output)
	output = output.split('#')

	#print(output)
	f1.close()
	# print('hello')

	# # print('a'+output)
	# output = output.split('#')
	# print(output)
	# output = ''
	file1 = open(inp.replace('in','out'), 'r')
	expected_output = file1.readlines()
	#print(expected_output)
	file1.close()

	index = 0
	sIndex = 0
	lineNo = 1
	bFlag = False
	while( lineNo < len(output) ):
	    # print('ads')
	    line = output[lineNo].split('\n')
	    #print(output[lineNo])
	    if( len(line) != 1 ):
	        #print(line)
	        for i in line[ :-1]:
	            # print(i)
	            if( re.match(i, expected_output[index][sIndex : ]) ):
	                index += 1
	                sIndex = 0
	            else:
	                bFlag = True
	                break

	        if( line[-1] != '' ):
	            op = re.match(line[-1], expected_output[index][sIndex : ])
	            if( op ):
	                sIndex += op.span()[1]
	            else:
	                bFlag = True

	    else:
	        # print(line[0])
	        if( op := re.match(line[0], expected_output[index][sIndex : ]) ):
	            sIndex += op.span()[1]
	        else:
	            bFlag = True

	    if( bFlag == True ):
	        print('wrong_output: ', output[lineNo - 1])

	        filename,lineNo = output[lineNo - 1].split(':')
	        file1 = open(filename)
	        s = file1.readlines()
	        print(s[int(lineNo)-1])
	        result =result +(output[int(lineNo)-1]) +'\n'
	        result =result + lineNo + '\t' + s[int(lineNo)-1]
	        file1.close()
	        #print('hello')
	        return result
	        break

	    lineNo += 2


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
				# print("here")
				# p.stdin.write('set $argument = 3\n')
				# p.stdin.write('source pygdb.py'+'\n')
				# p.stdin.write(inp+'\n')
				# print("For test case "+inp+":")
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

				# out , errors = p.communicate()
				# print(errors)
				# glob_list = out.split('\n')
				# c = 0
				# l = []
				# for i in glob_list:
				# 	if i.startswith('(gdb) quit'):
				# 		break
				# 	elif i.startswith('(gdb) '):
				# 		c = 1
				# 	elif c == 1:
				# 		# print(i)
				# 		l.append(i)

				# wrong_ouptut_list = []
				# flag = 1
				# for i in l:
				# 	if i.startswith('Breakpoint') and flag:
				# 		func_str = i
				# 		flag = 0
				# 		temp_str = ""
				# 	elif flag ==0:
				# 		if i.startswith("res"):
				# 			temp = i.split()[-1]
				# 			if temp == "0":
				# 				wrong_ouptut_list.append(["EMPTY",temp_str])
				# 			else:
				# 				wrong_ouptut_list.append([temp,temp_str])
				# 			c +=1
				# 			flag = 1
				# 		else:
				# 			if re.search('printf',i):
				# 				temp_str = i
				# print(wrong_ouptut_list)
				# corr_output_list = []
				# corr_output_file = open('out'+inp_files[inp_files.index(inp)][2:])
				# for i in corr_output_file.readlines():
				# 	# print(i)
				# 	corr_output_list.extend(i.split())
				# # print()
				# print(corr_output_list)
				# temp_ind = 0
				# for i in range(len(wrong_ouptut_list)):
				# 	if wrong_ouptut_list[i][0] != corr_output_list[i]:
				# 		temp_ind = i
				# 		wrong_str = wrong_ouptut_list[i][1]
				# 		break
				s+="\nDebugger Message:\n\n"
				# # print(f'matches till index:{temp_ind}\nline is:{wrong_str}')
				# s+="Wrong Output\n"
				# s+=func_str+'\n'
				# print(wrong_str)
				# s+=wrong_str+'\n'
				s += wrong_output(file_names,inp,inp_files) + '\n'
				s += valgrind_out(file_names, inp) + '\n'
		else:
			p.stdin.write('set $argument = 2\n')
			p.stdin.write('source pygdb.py'+'\n')
			p.stdin.write(' '.join(file_names)+'\n')
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