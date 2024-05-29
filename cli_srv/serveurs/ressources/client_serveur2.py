import socket
import threading

header = 64
format = "utf-8"
port = 5050
disconnect_msg = "DISCON"

server="192.168.1.59"
address=(server,port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)

def send(msg):
    msg_f = msg.encode(format)
    msg_length = len(msg_f)
    send_length = str(msg_length).encode(format)
    # (header - la longueur de la longueur)
    send_length += b' ' * (header - len(send_length))
    print(f"[{msg_f}] to send; initializing conversation with length [{msg_length}]")
    client.send(send_length)
    client.send(msg_f)

send("hello world")
send(disconnect_msg)
