#!/usr/bin/env python
# Author: Boumediene KADDOUR - OSCP, OSWP
# Created for learning purposes and Pentest Magazine article contribution
import socket, struct

class Injectme:
	def __init__(self):
            self.dmac = "\xaa\xbb\xcc\xdd\xee\xff"
            self.myMAC = "\xaa\xaa\xaa\xaa\xaa\xaa"
            self.eth_type = "\x08\x00"

	def packet(self):
		eth_header = struct.pack("!6s6s2s", self.dmac, self.myMAC, self.eth_type)
		return eth_header


obj = Injectme() 
pkt =  obj.packet()
s = socket.socket(socket.PF_PACKET,socket.SOCK_RAW, socket.htons(0x0800))
s.bind(("eth0", socket.htons(0x0800)))
s.send(pkt + "hi there")
