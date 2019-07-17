# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets , uic
import pandas as pd
import matplotlib.pylab as plt
from graph import main 
from cleanLog import main as cleanfile
from Clean import main as clean
import matplotlib
matplotlib.use('QT5Agg')
import os

#from matplotlib.backends.backend_qt5agg import FigureCanvas 
#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(584, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCleanFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnCleanFile.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.btnCleanFile.setObjectName("btnCleanFile")
        self.btnClean = QtWidgets.QPushButton(self.centralwidget)
        self.btnClean.setGeometry(QtCore.QRect(130, 20, 75, 23))
        self.btnClean.setObjectName("btnClean")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(320, 20, 231, 211))
        self.widget.setObjectName("widget")
        self.btnipWhois = QtWidgets.QPushButton(self.centralwidget)
        self.btnipWhois.setGeometry(QtCore.QRect(30, 240, 75, 23))
        self.btnipWhois.setObjectName("btnipWhois")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(190, 320, 75, 23))
        self.btnExit.setObjectName("btnExit")
        self.ipLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ipLineEdit.setGeometry(QtCore.QRect(140, 240, 113, 20))
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.btnStatistics = QtWidgets.QPushButton(self.centralwidget)
        self.btnStatistics.setGeometry(QtCore.QRect(30, 90, 75, 23))
        self.btnStatistics.setObjectName("btnStatistics")
        self.btnHeatMap = QtWidgets.QPushButton(self.centralwidget)
        self.btnHeatMap.setGeometry(QtCore.QRect(130, 90, 75, 23))
        self.btnHeatMap.setObjectName("btnHeatMap")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        
        # code to connect functionality 
        self.btnClean.clicked.connect(self.cleanfunc)   
        self.btnipWhois.clicked.connect(self.ipwhoisfunc)     
        self.btnExit.clicked.connect(self.exitfunc)       
        self.btnCleanFile.clicked.connect(self.cleanfilefunc)
        self.btnStatistics.clicked.connect(self.ipStatistics)
        self.btnHeatMap.clicked.connect(self.conectionHeatMap)
        
       
    def ipwhoisfunc(self):
        try:
            # whois()
            print (' test ')
        except Exception as e:
            print(e)
            
            
    def cleanfilefunc(self):
        try:
            cleanfile()
            print ('Task Finished !')
        except Exception as e:
            print(e)
        
        
    def exitfunc(self):
        try:
            sys.exit(app.exec_())
        except Exception as e:
            print(e)
    
    
    def singleIpMap(self):
        try:
            if os.path.exists("unique.csv"):
                data = pd.read_csv('unique.csv')
                data.Occurrences.value_counts().sort_index().plot()
                plt.xlabel('Number of occurrences')
                plt.ylabel('Unique addresses recorded')
            
        except Exception as e:
            print(e)
        
        
    def conectionHeatMap(self):
        try:
            if os.path.exists("log.csv"):
                data = pd.read_csv('log.csv')
                data['Time'] = pd.to_datetime(data.Time)
                data.Time.value_counts().sort_index().plot()
            
        except Exception as e:
            print(e)
        
        
    def ipStatistics(self):
        try:
            if os.path.exists("unique.csv"):
                data = pd.read_csv('unique.csv' ,skiprows = None)
                data = data.Occurrences.value_counts().sort_index().plot()
                # names labels x and y
                plt.xlabel('Number of occurrences')
                plt.ylabel('Unique addresses recorded')
            
        except Exception as e:
            print(e)
        
        
    def cleanfunc(self):
        try:
            # deletes tmp files if they are not going to be used by user
            clean()
            print ('Task Finished !')
        except Exception as e:
            print(e)
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnCleanFile.setText(_translate("MainWindow", "Clean File"))
        self.btnClean.setText(_translate("MainWindow", "Clean"))
        self.btnipWhois.setText(_translate("MainWindow", "Search IP"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.ipLineEdit.setPlaceholderText(_translate("MainWindow", "Enter ip here for who is seach"))
        self.btnStatistics.setText(_translate("MainWindow", "Statistics"))
        self.btnHeatMap.setText(_translate("MainWindow", "HeatMap"))
      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

