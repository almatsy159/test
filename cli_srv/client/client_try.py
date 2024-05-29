import sys
import os
import ipaddress
import socket
import sys

host,port = ('127.0.0.1',5566) # localhost
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

data = ""

"""
for i in range(len(sys.argv)):
    if i != 0:
        data += sys.argv[i]
if len(sys.argv) > 1:
    port = sys.argv[1]

    if len(sys.argv)> 2:
        host = sys.argv[2]
    else :
        host = "127.0.0.1"
else :
    port = 5566
    host = host = "127.0.0.1"
"""
for i in range(len(sys.argv)):
    if i != 0:
        data += sys.argv[i]



try :

    socket.connect((host,port))
    print("Client connected")
    a_ete_co = 1

    print(f"data to send : {data}")
    data = data.encode("utf8")
    print(f"encoded data {data}")
    socket.sendall(data)
    print("data sent !")



except ConnectionRefusedError :
    a_ete_co = 0
    print("Connection error")

finally:

    socket.close()
    print("socket closed")
