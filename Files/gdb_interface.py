from subprocess import *
import subprocess

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

# print(inp_files)

for inp in inp_files:
	p = Popen(['gdb', 'a.out'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines = True)
	if(inp == ""):
		p.stdin.write('r\n')
	else:
		print("For test case "+inp+":")
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
		elif i.startswith('(gdb)') and c == 1:	
			print("\n")
			print(i[6:])
			c+=1
		elif i.startswith('(gdb)') and c == 2:
			print("\n")
			print(i[6:])
			c+=1
		elif i.startswith('(gdb)') and c == 3:	break
		elif c == 1:	print(i)
		elif c == 2:	print(i) 
		elif c == 3:	print(i)
	print()
























# out = a.communicate()


# command = "./a.out < in03.txt"

# result = run(command, universal_newlines=True,shell = True, text = True)
# print(result.returncode, result.stdout, result.stderr)

# command = "./a.out < in03.txt "
# subprocess.call([command],shell = True)