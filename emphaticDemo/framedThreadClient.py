#! /usr/bin/env python3

# Echo client program
import socket, sys, re
import params
from framedSock import FramedStreamSock
from threading import Thread
import time

switchesVarDefaults = (
    (('-s', '--server'), 'server', "localhost:50001"),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )


progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug  = paramMap["server"], paramMap["usage"], paramMap["debug"]

if usage:
    params.usage()


try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

class ClientThread(Thread):
    def __init__(self, serverHost, serverPort, debug):
        Thread.__init__(self, daemon=False)
        self.serverHost, self.serverPort, self.debug = serverHost, serverPort, debug
        self.start()
    def run(self):
       s = None
       for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
           af, socktype, proto, canonname, sa = res
           try:
               print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
               s = socket.socket(af, socktype, proto)
           except socket.error as msg:
               print(" error: %s" % msg)
               s = None
               continue
           try:
               print(" attempting to connect to %s" % repr(sa))
               s.connect(sa)
           except socket.error as msg:
               print(" error: %s" % msg)
               s.close()
               s = None
               continue
           break

       if s is None:
           print('could not open socket')
           sys.exit(1)

       fs = FramedStreamSock(s, debug=debug)
       
       fname = input("What file are we sending?")
       #Check if it's a valid file
       if os.path.isfile(fname):
           #get file size
           fsize = os.path.getsize(fname)
    
           sock.send((str(size)+":"fname).encode())
           msg = sock.recv(100).decode()
           if msg == "READY TO RECEIVE":
               print(msg)
               with open(fname, 'rb') as fn:
                   btoSend = fn.read(100)
                   sock.send(btoSend)

                   #send till we run out
                   while bstoSend:
                       btoSend = fn.read(100)
                       sock.send(btoSend)
                print("Okay, all done")
                print(sock.recv(100).decode())
"""
       print("sending hello world")
       fs.sendmsg(b"hello world")
       print("received:", fs.receivemsg())

       fs.sendmsg(b"hello world")
       print("received:", fs.receivemsg())
"""
for i in range(100):
    ClientThread(serverHost, serverPort, debug)

