from PyQt5 import QtWidgets ,QtCore , QtGui
from Application import GUI
from Application import Clean_log
from Application import who_is
import sys


class MyQtApp(GUI.Ui_MainWindow , QtWidgets.QMainWindow):
    #used for conencting ui and code function together

    def __init__(self):
        super(MyQtApp , self).__init__()
        self.setupUi(self)
        #link buttong to def select log
        self.Tool_btn.clicked.connect(self.select_log)
        
        self.Clean_btn.clicked.connect(self.clean_log)
        
        self.WhoIs_btn.clicked.connect(self.Who_Is)


    def clean_log(self):
      
        print('test clean')

     
    def Who_Is(self):
       
        print('test Who is')
        
        
    def select_log(self):
       log_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select log')
       if log_path:
           self.lineEdit.setText(log_path)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    sys.exit(app.exec_())
