import socket

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

# ------------ PROXY CHAIN SETUP -----------------

# Proxy 1
A_ip = "proxyA.ip"
A_port = 8080

# Proxy 2
B_ip = "proxyB.ip"
B_port = 8080

# Step 1 — connect to Proxy A
s = connect(A_ip, A_port)

# Step 2 — ask Proxy A to connect to Proxy B
tunnel(s, B_ip, B_port)

# Step 3 — ask Proxy B (through A) to connect to Google
tunnel(s, "www.google.com", 80)

# Now you are chained:  You → A → B → Google
s.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
print(s.recv(4096).decode())
