import socket
import PyQt5.QtWidgets as qtw
import re
import os
import sys
import time
import threading

# this program seem to have been writen with windows and a special config doesn't work on my ubuntu...  , need to restudy it ...
x="$HOME"
data = "wsl ls"
data2="system.f\"echo {x}\""

host,port = 'localhost',x


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
        #Log(f"decoded data :{self.id} : {data}")

        """
        with open(f"log_srv.txt","w+") as file:
            file.write(f" at {signal_time} program {sys.argv[0]} rcv {data} ")
        """


class Server():
    def __init__(self,host='',port=5566,state=True):
        # if = None  !!!
        self.host=host
        self.port=port
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((self.host,self.port))

        Log(f"Serveur démarré associé au port {port}, mise en ecoute !")

        #print(dir(socket.listen()))
        while state == True:

            self.socket.listen()
            self.conn, self.address = self.socket.accept()
            # Log
            print("client connected")

            self.data = self.conn.recv(1024)
            self.data.decode("utf8")
            print(self.data)


            #self.my_thread = Thread(conn)
            #self.my_thread.start()


        self.conn.close()
        self.socket.close()


class Client():
    def __init__(self,data="",host="127.0.0.1",port=5566):

        self.data = ""
        #print(sys.argv)
        for i in range(len(sys.argv)):
            #if i != 0:
            self.data += sys.argv[i]+ ":"

        self.data += data


        #self.host,self.port = ('127.0.0.1',5566) # localhost
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        try :

            self.socket.connect((self.host,self.port))
            #print("Client connected")
            self.a_ete_co = 1

            #print(f"data to send : {self.data}")
            self.data = self.data.encode("utf8")
            #print(f"encoded data {self.data}")
            self.socket.sendall(self.data)
            #print("data sent !")



        except ConnectionRefusedError :
            self.a_ete_co = 0
            print("Connection error")

        finally:

            self.socket.close()
            print("socket closed")


class Data():

    def __init__(self,data,separator=".",type="string"):

        self.proto_data = data
        self.data= ""
        self.len_init = len(self.data)
        print("len data",len(data))
        self.separator = separator # may be a list
        self.type = type # cf mime type /sub_type

        for c in range(len(self.proto_data)) :
            print(f"{self.proto_data[c]} : {c}")
            if self.proto_data[c] == self.separator :
                self.prefix = self.data[0:c]
                self.data = self.data[c:]

    def extract(self,groups=None):
        list_of_group=[]
        if groups == None:
            list_of_group.append(self.separator)
        else :
            list_of_group = groups
        dict_pat_res={}
        pattern=""
        nb = len(list_of_group)
        for group in list_of_group :
            pattern = group
            search=re.compile(pattern)
            res = search.search(self.data)
            dict_pat_res[group] = res

        #search = re.compile(pattern)
        #x=search.search()
        return dict_pat_res


class Main(qtw.QWidget):
    def __init__(self):

        self.parent=super().__init__()
        self.state = False

        self.main = qtw.QHBoxLayout()
        self.setLayout(self.main)

        self.srv_gpb=qtw.QGroupBox("Server")
        self.srv_layout = qtw.QVBoxLayout()
        self.srv_gpb.setLayout(self.srv_layout)
        self.main.addWidget(self.srv_gpb)

        self.srv_output = qtw.QTextEdit()
        self.srv_layout.addWidget(self.srv_output)
        self.srv_run = qtw.QPushButton("run",clicked=self.run)
        self.srv_stop = qtw.QPushButton("stop",clicked=self.stop)
        self.srv_layout.addWidget(self.srv_stop)
        self.srv_layout.addWidget(self.srv_run)




        self.cli_gpb = qtw.QGroupBox("Client")
        self.cli_layout = qtw.QVBoxLayout()
        self.cli_gpb.setLayout(self.cli_layout)
        self.main.addWidget(self.cli_gpb)

        self.cli_gpb1 = qtw.QGroupBox("Info")
        self.cli_info_layout=qtw.QGridLayout()
        self.cli_gpb2 = qtw.QGroupBox("Command")
        self.cli_command_layout = qtw.QHBoxLayout()
        self.cli_gpb1.setLayout(self.cli_info_layout)
        self.cli_gpb2.setLayout(self.cli_command_layout)
        self.cli_target_srv = qtw.QLineEdit()
        #self.cli_target_srv = qtw.QComboBox()
        self.cli_btn1 = qtw.QPushButton("Submit",clicked = lambda : self.submit_data())
        self.cli_input = qtw.QLineEdit()
        self.cli_lab1 = qtw.QLabel("Server")
        self.cli_lab2 = qtw.QLabel("Port")
        self.cli_port = qtw.QLineEdit()


        self.cli_info_layout.addWidget(self.cli_lab1)
        self.cli_info_layout.addWidget(self.cli_target_srv)
        self.cli_info_layout.addWidget(self.cli_lab2)
        self.cli_info_layout.addWidget(self.cli_port)

        self.cli_command_layout.addWidget(self.cli_input)
        self.cli_command_layout.addWidget(self.cli_btn1)

        self.cli_layout.addWidget(self.cli_gpb1)
        self.cli_layout.addWidget(self.cli_gpb2)

        self.def_visibility()

        self.show()

    def check_data(self):
        print(self.data)
        is_ok =True
        #control here
        is_ok=False
        if is_OK == True:
            selfsubmit_data()

    def submit_data(self):
        data = self.cli_input.text()

        res1= os.popen("wsl pwd")
        working_dir = res1.read()
        output_content = f"{working_dir} : {data}\n"
        # here to servor
        """
        res2 = os.popen(data)
        output = res2.read()


        print(self.output)

        if isinstance(self.output,list):
            for i in data :
                output_content += i
        elif isinstance(self.output,str):
            output_content += output
        else :
            print(type,self.output)

        """
        print(data)
        self.host=self.cli_target_srv.text()
        self.port=self.cli_port.text()
        if self.host != '' and self.port != '':
            c1 = Client(data,self.host,int(self.port))
        else :
            c1 = Client(data)
        Log(f"client send to {self.host} port {self.port} => {output_content}")
        self.srv_output.setText(output_content)

    def def_visibility(self):
        if self.state == False:
            self.srv_run.setVisible(True)
            self.srv_stop.setVisible(False)
        else :
            self.srv_run.setVisible(False)
            self.srv_stop.setVisible(True)

    def run(self):
        self.state=True
        self.def_visibility()

        os.popen("python ./serveur_try.py")
        #server1=Server()

    def stop(self):
        self.state=False
        self.def_visibility()
"""
packet_list=[]
packet1=Data(data)
result = packet1.extract()
"""

app = qtw.QApplication([])
main=Main()

app.exec_()
