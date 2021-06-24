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

def loopFinder(pid,filenames):
    print(pid)
    filenames_list = filenames.split()
    # print(filenames_list)

    gdb.execute('attach '+pid)

    bt=gdb.execute('bt',to_string=True)
    # frame = gdb.selected_frame()
    # name=gdb.Frame.name(frame)
    # print(o)
    bt = bt.split('\n')
    frame_val = ''
    for i in range(len(bt)-1):
        bt_t = bt[i].split()
        s = re.match('.*\.c',bt_t[-1])
        s = s.group()
        if s in filenames_list:
            frame_val = bt_t[0][1:]
            break

    gdb.execute('frame '+frame_val)
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

# def wrong_out_finder(inp):
#     result = []
#     gdb.execute('b 80')
#     gdb.execute('b 85')
#     gdb.execute('r < '+inp,to_string=True)
#     o = gdb.execute("info locals",to_string=True)
#     # print(o.split())
#     # while(not re.search("program is not",o)):
#     while 1:
#         o = gdb.execute("n",to_string=True)
#         # l = o.split()
#         # if(re.search("Breakpoint",o)):
#         k = gdb.execute("info locals",to_string=True)
#         print(k)
#         result.append(k)


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
    loopFinder(pid,input())
else:
    wrong_out_finder(input())