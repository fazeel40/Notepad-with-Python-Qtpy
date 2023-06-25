from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
# from PyQt5.QtCore import Q
import sys
from PyQt5.uic import loadUi 

class my_app(QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()
        loadUi("NotePad.ui",self)
        
        self.current_path = None
        self.current_fontsize =8
        self.New.triggered.connect(self.New_)
        self.Save.triggered.connect(self.Save_)
        self.Save_As.triggered.connect(self.Save_As_)
        self.Open.triggered.connect(self.Open_)
        self.Undo.triggered.connect(self.Undo_)
        self.Redo.triggered.connect(self.Redo_)
        self.Copy.triggered.connect(self.Copy_)
        self.Cut.triggered.connect(self.Cut_)
        self.Paste.triggered.connect(self.Paste_)
        self.Light.triggered.connect(self.Light_)
        self.Dark.triggered.connect(self.Dark_)
        self.inc_size.triggered.connect(self.Inc_Size_)
        self.dec_size.triggered.connect(self.Dec_Size_)
    def New_(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")
    def Open_(self):
        self.textEdit.clear()
        fname = QFileDialog.getOpenFileName(self,"Open File","E:\\","Text files(*.txt)")
        self.setWindowTitle(fname[0])
        with open(fname[0],"r") as f:
            content = f.read()
        self.textEdit.setText(content)
        self.current_path = fname[0]
    def Save_(self):
        if self.current_path is not None:
            content = self.textEdit.toPlainText()
            with open(self.current_path,"w") as f1:
                f1.write(content) 
            f1.close()
        else:
            self.Save_As_()
    def Save_As_(self):
        pathname = QFileDialog.getSaveFileName(self,"Save File","E:\\","Text files(*.txt)")
        fileText = self.textEdit.toPlainText()
        with open(pathname[0],"w") as f:
            f.write(fileText)
        self.current_path=pathname[0]
        self.setWindowTitle(pathname[0])
    def Undo_(self):
        self.textEdit.undo() 
    def Redo_(self):
        self.textEdit.redo()
    def Copy_(self):
        self.textEdit.copy()
    def Cut_(self):
        self.textEdit.cut()
    def Paste_(self):
        self.textEdit.copy()
    def Light_(self):
        self.setStyleSheet("")
    def Dark_(self):
        self.setStyleSheet('''QWidget{
background: rgb(33,33,33);
color:"white";
}
QTextEdit{
background: rgb(46,46,46);
color:"white";
}
QMenuBar::item:selected{
color:"black";
}
''')
    def Inc_Size_(self): 
        self.current_fontsize+=1
        self.textEdit.setFontPointSize(self.current_fontsize)
    def Dec_Size_(self):
        self.current_fontsize-=1
        self.textEdit.setFontPointSize(self.current_fontsize)
    
         
def window():
    app = QApplication(sys.argv)
    win = my_app()
    win.show()
    win.setWindowTitle("My Note Pad\\New Text File.txt")
    sys.exit(app.exec_())
window()