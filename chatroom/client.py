from socket import *
import sys,os

#发送消息
def send_msg(s,name,addr):
    while True:
        text = input('speak:')
        #输入quit退出
        if text.strip() == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(),addr)
            sys.exit('quit chatroom')
        msg = 'C %s %s'%(name,text)
        s.sendto(msg.encode(),addr) 

#接收消息
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        if data.decode() == 'EXIT':
            sys.exit(0)
        print(data.decode()+ '\nspeak:',end='')

#实现创建套接字，登录：创建子进程
def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)

    while True:
        name = input('please input name:')
        msg = 'L ' + name
        #发送登录请求
        s.sendto(msg.encode(),ADDR)
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print('you have access to the chatroom')
            break
        else:
            #不成功服务端会回复不允许登录原因
            print(data.decode())

    #创建父子进程
    pid = os.fork()
    if pid < 0:
        sys.exit('ｃｒｅａｔｅ process faile')
    elif pid == 0:
        send_msg(s,name,ADDR)
    else:
        recv_msg(s)

if __name__ == '__main__':
    main()