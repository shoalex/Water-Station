from db import dbconnect
import threading
import socket

db=dbconnect("data.db")
t=threading.Thread(target=db.connect)
t.start()
t.join()

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
clients = []
def threadFunc(conn):
    with conn:
        while True:
            data = conn.recv(1024)
            recived=data.decode().split(",")
            if len(recived)==3:
                t = threading.Thread(target=db.insert(recived[0],recived[1],recived[2]))
                t.start()
                t.join()

            if not data:
                clients.remove(conn)
                break
            print("Data received from client: ",data.decode())
            conn.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        clients.append(conn)
        t = threading.Thread(target=threadFunc, args=(conn,))
        t.start()
