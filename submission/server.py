import socket

from _thread import *
import threading

print_lock = threading.Lock()

def threaded(c):
    while True:
        data = recv(1024)
        if not data:
            print('Bye')
            print_lock.release()
            #lock release before exiting
            break

        data = data[::-1]
        #for reversing string
        c.send(data)
    c.close()

def Nain():
    host = ""
    port = 50001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind( (host, port) )
    print("socket binded to post", port)

    s.listen(5)
    print("socket is listening")

    
    while True:

        c, addr = s.accept()
        #connecting...
        print_lock.acquire()
        #lock acquired...
        print('Connected to :', addr[0], ':', addr[1])
        
        start_new_thread( threaded, (c,) )
    s.close()

if __name__ == '__main__':
    Main()
