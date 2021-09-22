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

# functions for interactions 
 
# functions for modal version 
 
# functions for modeless version 
 
# connect signals and other initializations 
 
button.clicked.connect(dialogBox.exec_) # invoke dialog modal version 
 
# run the program 
  
mainWindow.show() 
 
sys.exit(app.exec_()) 
