#!/usr/bin/env python
# Author: Boumediene KADDOUR - OSCP, OSWP
# Created for learning purposes and Pentest Magazine article contribution

from checksum import checksum
import socket, struct
from random import randint
def ICMP():
	id = randint(0, 0xFFFF)
	icmp = struct.pack("!BBHHH", 8,0, 0, id, 1)
	chksum = checksum(icmp)
	icmp_pkt = struct.pack("!BBHHH", 8, 0, socket.htons(chksum), id, 1)
	return icmp_pkt

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
s.sendto(ICMP(), ("172.16.122.1",0))

