#!/usr/bin/env python
# Author: Boumediene KADDOUR - OSCP, OSWP
# Created for learning purposes and Pentest Magazine article contribution

import socket 
import struct 
from random import randint
from sys import argv

class InjectMe:
	def __init__(self,source=None, dest=None):
		##### IP ####
		self.version = 4
		self.ihl = 5
		self.tos = 0
		self.tlen = 0
		self.id = randint(50000, 60000)
		self.flags = 0
		self.offset = 0
		self.ttl = 64
		self.protocol = socket.IPPROTO_TCP
		self.checksum = 0
		self.source = socket.inet_aton(source)
		self.dest = socket.inet_aton(dest)
		
	def packing_ip_header(self):
		# Packing IP header
		ver_ihl = (self.version << 4) + self.ihl
		flags_offset = (self.flags << 13) + self.offset
		ip_header = struct.pack('!BBHHHBBH4s4s', ver_ihl,
			    self.tos,
		   	  self.id,
			    self.tlen,
			    flags_offset,
			    self.ttl,
			    self.protocol,
			    self.checksum,
			    self.source,
			    self.dest)
		return ip_header

def main(source, dest):
    obj = InjectMe(source, dest)
    iphdr = obj.packing_ip_header()
    pkt = iphdr
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    s.sendto(pkt,(dest,0))
    print "[+] PKT injected :)"



if __name__ == "__main__":
    if len(argv) != 3:
        print """
Usage:	
       	%s <srcip> <dstip>
	      """%argv[0]
	exit(1)
    else:
        source = argv[1]
        dest = argv[2]
        main(source, dest)

