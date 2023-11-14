# a demo script to trace tcp_connect call graph with function_graph tracer

import os,sys,socket

def echo(s, f):
    fp = open(f, 'w')
    fp.write(str(s))
    fp.close()

def cat(f):
    with open(f) as fh:
        print(fh.read())

os.chdir('/sys/kernel/debug/tracing')
pid = os.getpid()
echo(pid, 'set_ftrace_pid')
echo('function_graph', 'current_tracer')
#old kernel:
echo('SyS_connect','set_graph_function')
echo(15, 'max_graph_depth')
echo(1, 'tracing_on')
#new kernel
#echo('__x64_sys_connect','set_graph_function')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)
try:
    s.connect(('10.10.10.10', 80))
except Exception as e:
    print(e)
s.close()

cat('trace')
echo('nop', 'current_tracer')
echo(0, 'tracing_on')




