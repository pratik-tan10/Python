# imports  
 
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QDialog 
 
# set up app and GUI  
 
app = QApplication(sys.argv) 
   
mainWindow = QMainWindow() 
mainWindow.resize(400,200) 
mainWindow.setWindowTitle("PyQt5 example 3") 
mainWindow.setCentralWidget(QWidget()) 
 
layout = QGridLayout(mainWindow.centralWidget()) 
 
button = QPushButton("Open dialog ...") 
layout.addWidget(button,0,0) 
   
dialogBox = QDialog() 
dialogBox.setWindowTitle("The world's weirdest dialog box") 
