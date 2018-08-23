import os

print('Process (%s) start...' % os.getpid())

pid = os.fork()

if pid == 0:
    print('Child process (%s), ppid is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process.' % os.getpid())
