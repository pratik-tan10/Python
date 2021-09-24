import sys, csv 
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyle, QFileDialog, QDialog, QMessageBox, QSizePolicy 
from PyQt5.QtGui import QStandardItemModel, QStandardItem,  QDoubleValidator, QIntValidator 
from PyQt5.QtCore import QVariant 
from PyQt5.Qt import Qt
 
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView as WebMapWidget
except:
    from PyQt5.QtWebKitWidgets import QWebView as WebMapWidget
 
import gui_main  
import gui_newshapefile 
import core_functions 
 
# ======================================= 
# GUI event handler and related functions 
# ======================================= 
 
#========================================== 
# create app and main window + dialog GUI 
# =========================================  
 
#========================================== 
# connect signals 
#========================================== 
 
#================================== 
# initialize global variables 
#================================== 
 
#============================================ 
# test availability and if run as script tool 
#============================================ 
 
#======================================= 
# run app 
#======================================= 
mainWindow.show() 
sys.exit(app.exec_()) 
