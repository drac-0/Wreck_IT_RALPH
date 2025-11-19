#!/usr/bin/env python3

import socket
from fp.fp import FreeProxy

iteration = 1

def generateproxy():
	proxyurl = FreeProxy(rand=True).get()
	proxy = (proxyurl.split("//")[1]).split(":")
	ip = proxy[0]
	port = int(proxy[1])
	
	return ip, port

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	dest = generateproxy()
	print(dest)

	try:
		s.connect(dest)		
		print(f"SUCCESSFULY CONNECTED TO THE PROXY WITH IP") 
	
	except:
		print("FAILED")

	print(f"sending request to the proxy.")
	anotherurl = FreeProxy(rand=True).get()
	print(anotherurl)
	req = (	
		f"CONNECt {anotherurl} HTTP/1.1\r\n"
		f"Host: {anotherurl}\r\n"
		"Connection: close\r\n"
		"\r\n"
)

	
	s.sendall(req.encode())	
	data = b""
	while b"\r\n\r\n" not in data:
		data += s.recv(4096)

	if b"200" not in data.split(b"\r\n")[0]:
       		raise Exception("CONNECT failed: " + data.decode())
	
	

	s.close()
	iteration += 1
