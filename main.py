import json
import socket
import struct
import threading

# создаем сокет
sock = socket.socket()
# подключаемся к 127.0.0.1:9090
sock.connect(('127.0.0.1', 9090))
admin = {
    "id": "ADMIN"
}


def check(conn):
    while True:
        data_size = b''

        while len(data_size) < 4:
            data_size += conn.recv(4 - len(data_size))

        size = struct.unpack("<I", data_size)[0]

        data_size = b''

        while len(data_size) < size:
            data_size = conn.recv(size - len(data_size))

        data = data_size.decode("utf-8")
        print(data)


threading.Thread(target=check, args=[sock]).start()


while True:
    a = input()
    admin["message"] = a
    info = json.dumps(admin)
    info2 = struct.pack("<I", len(info))
    sock.send(info2)
    sock.send(info.encode("utf-8"))