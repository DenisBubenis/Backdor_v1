import socket

sock = socket.socket()

sock.connect(('127.0.0.1', 9090))
print("connected")
while True:
    data = sock.recv(1024)
    print(data)
    sock.send(b"pupa")