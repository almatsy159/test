import socket
import threading

header = 64
format = "utf-8"
port = 5050
disconnect_msg = "DISCON"
host = socket.gethostbyname(socket.gethostname())
print( f"serveur set up on port {port} at adrress : {host}({socket.gethostname()}) ")
#logs


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = (host,port)
server.bind(address)

def handle_client(conn,address):
    print(f"new connection :{address} connected")
    connected = True
    while connected:
        msg_length = conn.recv(header).decode(format)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(format)
            if msg == disconnect_msg:
                connected = False
            print(f"[{address}] send {msg}")
    conn.close()


def start():
    server.listen()
    print(f"[LISTENNING] on {server}")
    while True:
        conn, address = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,address))
        thread.start()
        print(f"active connection {threading.activeCount() -1 }")



print("server is starting")
start()
