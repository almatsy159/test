import PyQt5.QtWidgets as qtw
import sys

liste_doc=["doc1","doc2"]

doc1 = ["sec1","sec2"]
s1d1 = ["titlte1d1","title2d2"]
s2d1 = ["titlte1d3","title2d3"]
doc2 = ["sec1","sec2"]
s1d2 = ["titlte1d1","title2d2"]
s2d2 = ["titlte1d1","title2d2"]

class MainApp(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unik Doc")
        

        #x=qtw.QTreeWidgetItem()
        #self.treeWidget.SetColumnCount(1)
        #b1=self.setLayout(qtw.QVBoxLayout())
        #qtw.QTreeWidgetItem(liste_doc[0])
        #self.treeWidget.addTopLevelItem(b1)


app = qtw.QApplication(sys.argv)
main= MainApp()

        
        
