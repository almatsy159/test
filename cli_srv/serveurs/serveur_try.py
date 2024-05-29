# client serveur
import socket
# packet handler
import threading
# time of exec ...
import time
# sys argv ...
import sys
# DB
import mysql.connector as mc

import PyQt5.QtWidgets
# module perso
#import ressource


db_host='localhost'
"""
db_usr=input('username :')
db_pwd=input('password :')
"""

host,port = ('',54321)
class Host():
    pass
    #self.name

class Log():
    id = 0
    def __init__(self,log,file=f"log_srv.txt",type="notify"):
        self.log=log
        self.file=file
        self.type=type
        self.date=time.time()
        self.id = Log.id
        Log.id +=1
        with open(file,"a+") as f:
            str=f"{self.date}:{self.id}_{type}#{self.log}\n"
            print(str)
            f.write(str)

    def write_log(self):
        pass #bd and read !!

    def read_log(self,expr="(.{8}:[0-9]*_.*#)(.*)",file="log_srv.txt"):
        x=re.compile(expr)
        with open(file,"r+") as f:
            for line in f.readlines():
                print(x.match(line).group(2))


l1=Log(f"Starting {sys.argv[0]}")

class DB():
    def __init__(self,host='localhost',db='srv_db',usr='root',pwd=''):

        self.host =host
        self.db = db
        self.usr = usr
        self.pwd = pwd
        Log("srv_connected")
        self.conn = mc.connect(host=self.host,database=self.db,user=self.usr,password=self.pwd)

    def request(self,rqt):

        Log(f"Making a request : \n{rqt}")
        c=self.conn.cursor()
        c.execute(rqt)
        res=c.fetchall()
        str_log=""
        for i in res :
            str_log += str(i) +"\n"
        c.close()
        return res


db = DB()
tables=db.request("SHOW TABLES")
Log(f"tables : {tables}")

class Thread(threading.Thread):
    id = 0

    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn
        self.id = Thread.id
        Thread.id += 1

    def run(self):
        signal_time = time.time()
        data = self.conn.recv(1024)
        #Log(f"undecoded data : {data}")
        data = data.decode("utf8")
        Log(f"decoded data :{self.id} : {data}")

        """
        with open(f"log_srv.txt","w+") as file:
            file.write(f" at {signal_time} program {sys.argv[0]} rcv {data} ")
        """


socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((host,port))

Log(f"Serveur démarré associé au port {port}, mise en ecoute !")

#print(dir(socket.listen()))
while True:

    socket.listen()
    conn, address = socket.accept()
    Log("client connected")
    """
    data = conn.recv(1024)
    data.decode("utf8")
    print(data)
    """
    my_thread = Thread(conn)
    my_thread.start()


conn.close()
socket.close()

l1.read_log()
