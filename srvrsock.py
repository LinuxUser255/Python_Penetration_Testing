#!/usr/bin/env python 3

import socket

#Bind to a specified addy & port
#And listen for incoming TCP coms
SRV_ADDR = input("Type server IP: ")
SRV_PORT = int(input("Type the server port: "))

#Default family socket: AF_INET, default socket: SOCK_STREAM
s = socket.sockets(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT)) #socket bound to addy&port
s.listen(1)                  #listen for incoming connections 

print(" Server started! Waiting for connections..")
connection, address = s.accept() #socket object & client address
print("Client connected with address: ", address)
while 1:                        #1 specs the max number of queued connects  
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b'--Message Received --\n')
    print(data.decode('utf-8'))
connection.close()


