#!/usr/bin/env python3
import socket 

ip = socket.gethostbyname('www.google.com')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
port = 80
ipv2 = "209.13.96.171"

s.connect((ip,port))
print(s.getsockname())

