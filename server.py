import socket
import threading
import os
HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 5000))


clientes = []

def manejar_cliente(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            for c in clientes:
                if c != conn:
                    c.sendall(data)
        except:
            break
    conn.close()
    clientes.remove(conn)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

print("Servidor listo, esperando jugadores...")

while True:
    conn, addr = server.accept()
    print("Jugador conectado:", addr)
    clientes.append(conn)
    threading.Thread(target=manejar_cliente, args=(conn,)).start()

