#waitpid.py
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
    while True:
        sleep(1)
        #通过非阻塞的形式捕获进程退出
        pid,status = os.waitpid(-1,os.WNOHANG)
        print(pid,status)
    while True:
        pass