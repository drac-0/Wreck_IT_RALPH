#!/usr/bin/env python3

import socket
from fp.fp import FreeProxy

iteration = 1

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	proxyv2 = FreeProxy(rand=True).get()
	proxyv3 = (proxyv2.split("//")[1]).split(":")
	ip = proxyv3[0]
	port = int(proxyv3[1])
	print(f"in {iteration} ip proxy : {ip}, and port : {port}")

	try:
		s.connect((ip,port))		
		print(f"SUCCESSFULY CONNECTED TO THE PROXY WITH IP {ip} and port {port} ")

	except:
		print("FAILED")

	s.close()
	iteration += 1

