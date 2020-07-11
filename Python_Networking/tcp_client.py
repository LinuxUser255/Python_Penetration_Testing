#!/usr/bin/env python

import socket

target_host = "google.com"
target_port = 80

#creating a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connnecting the client
client.connect((target_host, target_port))

#sending data
client.send("GET/HTTP.1.1\r\nHost: google.com\r\n\r\n")

#receiving data
response = client.recv(4096)


print response
