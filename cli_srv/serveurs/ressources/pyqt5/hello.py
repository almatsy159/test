import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainApp(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First App")
        # vertical layout
        self.setLayout(qtw.QVBoxLayout())

        label1=qtw.QLabel("Hi you, please give me your name !")

        label1.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(label1)

        #entry1=qtw.QLineEdit()
        #entry1.setObjectName("name")
        #self.layout().addWidget(entry1)
        #entry1.setText("default")

       # combo box or (double)spin box (self,val,max,min,singleStep,prefix,suffix )
        cb = qtw.QComboBox(self,editable=True,insertPolicy=qtw.QComboBox.InsertAtBottom)
        cb.addItem("opt1",1)
        cb.addItem("opt2",qtw.QWidget)
        cb.addItem("opt3","other_stuff")
        cb.addItems(["One","Two","Three"])
        cb.insertItem(2,"Third")

        self.layout().addWidget(cb)

        print("globals : :",globals())
        print("qt widget :",dir(qtw))
        text = qtw.QTextEdit(self,lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                #plainText="This is real text!",
                #html="<center><h1> Big <em>Header</em> </h1></center>",
                acceptRichText=True,
                lineWrapColumnOrWidth=50,
                placeholderText="Hello World",
              readOnly=False)
        self.layout().addWidget(text)

        btn1=qtw.QPushButton("Press Me!",clicked=lambda:press_it())


        self.layout().addWidget(btn1)

        self.show()

        def press_it():
            label1.setText(f'u picked {cb.currentText()} and typped {text.toPlainText()}') #index  or data
            text.setPlainText("Entry validate")
            #entry1.setText("")

app= qtw.QApplication([])
mw=MainApp()

app.exec_()
