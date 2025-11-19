import socket
from fp.fp import FreeProxy

# get a random HTTP proxy
proxy_url = FreeProxy(rand=True).get()
ip_port = proxy_url.split("//")[1]
ip, port = ip_port.split(":")
port = int(port)

# connect to the proxy
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
print(f"Connected to proxy {ip}:{port}")

# send a full HTTP GET request (the proxy will fetch it for you)
request = (
    "GET http://www.google.com/ HTTP/1.1\r\n"
    "Host: www.google.com\r\n"
    "Connection: close\r\n"
    "\r\n"
)

s.sendall(request.encode())

response = b""
while True:
    data = s.recv(4096)
    if not data:
        break
    response += data

print(response.decode(errors="replace"))
s.close()
