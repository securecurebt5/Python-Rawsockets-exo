#!/usr/bin/env python
# Author: Boumediene KADDOUR - OSCP, OSWP
# Created for learning purposes and Pentest Magazine article contribution
# Basic echo-server created for learning purposes

# Import the socket module
import socket

# defining the server IP and PORT
IP = "172.16.122.200"
PORT = 4545
server = (IP, PORT)

# Create the socket instance
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# allow address reuse
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the specified address and port
s.bind(server)
# Listen and start accepting connections
s.listen(100)
c, addr = s.accept()

# in case a connection established
if c:
    # print the remote address
    print "Connection from:", addr
    # enter a loop
    while True:
        try:
            # start receiving data with a buffer of 1024 Bytes
            data = c.recv(1024)
            # send back the received data
            c.sendall("server says: " + data)
        # exit when CTRL+C is passed
        except KeyboardInterrupt:
            exit(0)






