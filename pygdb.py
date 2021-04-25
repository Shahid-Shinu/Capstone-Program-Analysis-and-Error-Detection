import gdb
import subprocess
import sys

def segFinder(inp):
    gdb.execute('r < '+inp,to_string=True)
    print()
    o=gdb.execute('info locals',to_string=True)
    if(o != ""):
        print("Local Varaibles:")
        print(o)
    o=gdb.execute('bt',to_string=True)
    if(o != ""):
        print("Back Trace:")
        print(o)

def loopFinder(pid):
    print(pid)

    gdb.execute('attach '+pid)

    o=gdb.execute('bt',to_string=True)
    # frame = gdb.selected_frame()
    # name=gdb.Frame.name(frame)
    o=o.split("\n")
    # print(o)
    o=o[-2].split()[0]

    o = o[1:]
    print()
    gdb.execute('frame '+o)
    print()
    gdb.execute('down',to_string=True)
    # o = o.split('\n')
    # o = o[-1].split()
    print()
    gdb.execute('l')
    print()

    o=gdb.execute('info locals',to_string=True)
    if(o != ""):
        print()
        print("Local Varaibles:")
        print(o)

    o=gdb.execute('bt',to_string=True)
    if(o != ""):
        print()
        print("Back Trace:")
        print(o)

    gdb.execute('kill')
    #gdb.execute('next')


    #for i in range(100):
            #gdb.execute('n')
    #gdb.execute('step')
    #print('hi')
    #gdb.execute('quit')

def wrong_out_finder(inp):
    result = []
    gdb.execute('b 80')
    gdb.execute('b 85')
    gdb.execute('r < '+inp,to_string=True)
    o = gdb.execute("info locals",to_string=True)
    # print(o.split())
    # while(not re.search("program is not",o)):
    while 1:
        o = gdb.execute("n",to_string=True)
        # l = o.split()
        # if(re.search("Breakpoint",o)):
        k = gdb.execute("info locals",to_string=True)
        print(k)
        result.append(k)


# result = subprocess.run(['pidof', 'a.out'], stdout=subprocess.PIPE, universal_newlines = True, text = True)
# pid = result.stdout
# print(pid)
# loopFinder(pid)
# print(sys.arg)
# segFinder(input())
o = gdb.execute('print $argument',to_string=True)
arg = int(o.split()[-1])
# print("arg is",arg)

if arg == 1:
    segFinder(input())
elif arg == 2:
    result = subprocess.run(['pidof', 'a.out'], stdout=subprocess.PIPE, universal_newlines = True, text = True)
    pid = result.stdout.split()[-1]
    loopFinder(pid)
else:
    wrong_out_finder(input())