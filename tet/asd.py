import socket

proxy_host = '109.68.189.22'      # your proxy IP
proxy_port = 54643

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((proxy_host, proxy_port))

# send a GET with the full URL (proxy expects the full URL)
request = (
    "GET http://www.google.com/ HTTPS/1.1\r\n"
    "Host: www.google.com\r\n"
    "Connection: close\r\n"
    "\r\n"
).encode('utf-8')
s.sendall(request)

resp = b''
while True:
    data = s.recv(4096)
    if not data:
        break
    resp += data

print(resp.decode('utf-8', errors='replace'))
s.close()
