
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from objprint import op
import os

class App_BG():
    # read/write file; handle open/close window and widget ,their pos and param the data...; etc ...
    id=0
    def __init__(self):
        self.object_dict={}


class App_UI(qtw.QWidget):
    
    def __init__(self,bg):
        master=super().__init__()
        self.setWindowTitle("DU New")
        self.bg=bg
        self.setLayout(qtw.QVBoxLayout())

        self.t1=self.add_textEdit("t1","Input here")
        self.t2=self.add_textEdit("t2","Output there",True)
        #print(str(self.t1).read())
        self.layout().addWidget(self.t1)
        self.layout().addWidget(self.t2)
        
        self.b1=self.add_button("b1")
        self.layout().addWidget(self.b1)
        
        self.l1=self.add_label("l1","","Helvetica",18)
        self.layout().addWidget(self.l1)

        print(self.bg.object_dict)
        print(self.t1)
        self.show()
    
    def add_label(self,name,text,font,size):
        x=name
        name=qtw.QLabel(text)
        name.setFont(qtg.QFont(font,20))
        self.setDict("label",x,name)
        return name

    def add_textEdit(self,name,text="Hello",ro=False):
        """
        flag=0
        for i,j in self.bg.object_dict:
            if i == "textEdit":
                flag=1
        if flag == 0:
            self.bg.object_dict["textEdit"]={}
            """
        x=name
        name = qtw.QTextEdit(self,lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                #acceptRichText=True,
                lineWrapColumnOrWidth=100,
                readOnly=ro,
                placeholderText=text)
        """
        #self.layout().addWidget(name)
        
        name.setObjectName(x)
        self.bg.object_dict["textEdit"][self.bg.id]=name
        self.bg.id += 1
        """
        self.setDict("textEdit",x,name)
        return name

    def setDict(self,val,name,address):
        flag=0
        for i,j in self.bg.object_dict.items():
            if i == val:
                flag=1
        if flag==0:
            self.bg.object_dict[val]={}
        address.setObjectName(name)
        self.bg.object_dict[val][self.bg.id]=address
        self.bg.id +=1

    def add_button(self,name,text="Press"):
        x=name
        name =qtw.QPushButton(text,clicked=lambda:self.pressed())
        self.setDict("pushButton",x,name)
        return name

    def pressed(self):
        self.l1.setText(f"{self.t1.toPlainText()}")
        x=os.popen(f"{self.t1.toPlainText()}")
        print("x: ",x,"; and type of x",type(x))
        #self.t2.setPlainText("{}".format(os.popen(f"{self.t1.toPlainText}")))
        if x :
            self.t2.clear()
            output=x.read()
            self.t2.insertPlainText(output)

bg=App_BG()
app=qtw.QApplication([])
main=App_UI(bg)

app.exec()
