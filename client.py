#!/usr/bin/env python3
# Author: Boumediene KADDOUR - OSCP, OSWP
# Created for learning purposes and Pentest Magazine article contribution
# Basic echo-server

# import the socket module
import socket

# define the server IP & PORT
IP = '172.16.122.200'
PORT = 4545
server = (IP, PORT)

# Create the socket instance
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the remote server
s.connect(server)

# enter a loop
while True:
        # get msg from user input
        msg = raw_input("msg: ")
        # send the msg
	s.sendall(msg)
        # receive and print data
	data = s.recv(1024)
	print data



