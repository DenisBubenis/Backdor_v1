import socket
import threading
import time

connections = []
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)

def sender():
    global connections
    while True:
        for conn in connections:
            conn.send(b"lupa")

        time.sleep(3)

def socketReceiver(conn):
    print("listening to", conn)
    while True:
        data = conn.recv(1024)
        print("received", data, "from", conn)

t = threading.Thread(target=sender)
t.start()

while True:
    conn, addr = sock.accept()
    print(addr)
    connections.append(conn)

    threading.Thread(target=socketReceiver, args=[conn]).start()