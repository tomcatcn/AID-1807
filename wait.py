#wait.py
import os
from time import sleep

pid = os.fork()

if pid < 0 :
    print('create process failed')
elif pid == 0:
    sleep(3)
    print('child process exit',os.getpid())
    os._exit(2)
else:
    pid,status = os.wait()
    print(pid,status)
    while True:
        pass