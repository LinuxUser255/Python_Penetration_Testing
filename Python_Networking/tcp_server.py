#!/usr/bin/env python

import socket
import threading

bind_ip "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)

#server loops awaiting incoming connection
print "[*] Listening on %s:%d" % (bind_ip,bind_port)

def handle_client(client_socket):
    
    #Print what the client sends
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request

    #return a packet
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client,addr = server.accept()
    print"[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

#create client thread to handle incoming data
client_handler = threading.Thread.Thread(target=handle_client,args=(client,))
cliient_handler.start()

