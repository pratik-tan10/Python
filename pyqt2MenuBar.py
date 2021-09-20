
import sys 
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStyle 
 
app = QApplication(sys.argv) 
 
mainWindow = QMainWindow() 
mainWindow.resize(400,200) 
mainWindow.setWindowTitle("PyQt5 example 2") 
 
fileMenu = mainWindow.menuBar().addMenu('&File')  
optionsMenu = mainWindow.menuBar().addMenu('&Options') 
 
exitAction = QAction(app.style().standardIcon(QStyle.SP_DialogCancelButton), '&Exit', mainWindow) 
exitAction.setShortcut('Ctrl+Q') 
exitAction.setStatusTip('Exit application') 
exitAction.triggered.connect(app.quit) 
 
fileMenu.addAction(exitAction) 
 
mainWindow.statusBar().showMessage('Waiting for your commands...') 
 
mainWindow.show() 
 
sys.exit(app.exec_()) 
