#!/usr/bin/env python3


import socket


# Network socket: start a client that initiates a connection to a Python Server
# use the connect function
SRV_ADDR = input("TYpe server IP: ")
SRV_PORT = int(input("Type the server port: ")


#The change is in the block below using my_sock instead of s.bind
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((SER_ADDR, SER_PORT))
print("Connection established")

messsage = input("message to send: ")
my_sock.sendall(message.encode())
my_sock.close()







