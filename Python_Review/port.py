#!/usr/bin/env python3

#Reading user input

target = input("Enter the IP to scan: ")
port = input("Enter the port number scan: ")

port = int(port.split('-') [0])


print("Scanning host", target, 'port', port)

