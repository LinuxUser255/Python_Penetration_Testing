#!/usr/bin/env python3

#Client

import socket

HEADER = 64
PORT = 4444
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "Connection closed"


#the client's socket object:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("qwerty is a horrible password.")
input() 
send("And no, password1 is even worse.")
input() 
send("Use common sense.")


send(DISCONNECT_MESSAGE)
