#!/usr/bin/env python3

import socket
from fp.fp import FreeProxy


def generateproxy(a) :
	proxy = FreeProxy(rand=True).get()
	ipport = (proxy.split("//")[1]).split(":")
	ip = ipport[0]
	port = ipport[1]

	return ip, port #i just learn that in python when you return more than 1 data in function, the data type output would be tuple

#i don't think this function is necessary :(
def connect(host, port):
    s = socket.socket()
    s.connect((host, port))
    return s

def tunnel(s, host, port):
    req = f"CONNECT {host}:{port} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    s.sendall(req.encode())

    data = b""
    while b"\r\n\r\n" not in data:
        data += s.recv(4096)

    if b"200" not in data.split(b"\r\n")[0]:
        raise Exception("CONNECT failed: " + data.decode())



url1 = generateproxy(0)
ip1 = url1[0]
port1 = int(url1[1])

url2 = generateproxy(1)
ip2 = url2[0]
port2 = int(url2[1])

print(ip1,port1)
print(ip2,port2)

print("connecting to the proxy 1")
s = connect(ip1,port1)

print("connecting to the proxy 2")
tunnel(s, ip2, port2)

tunnel(s, "www.google.com", 80)

s.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
print(s.recv(4096).decode())



