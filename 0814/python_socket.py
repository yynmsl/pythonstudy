# -*- coding: utf-8 -*-

from socket import *
import time

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSperSock = socket(AF_INET,SOCK_STREAM)
tcpSperSock.bind(ADDR)
tcpSperSock.listen(5)

while True:
    print 'waiting for connection'
    time.sleep(1)
    print 2
    tcpSperSock,addr = tcpSperSock.accept()
    print '...connection from ：',addr
    while True:
        data = tcpSperSock.recv(BUFSIZ)
        if not data:
            break
        tcpSperSock.send('[%s]%s'%(time.ctime(),data))
    tcpSperSock.close()
