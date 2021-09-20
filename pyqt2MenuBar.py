import sys 
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStyle, QFileDialog, QMessageBox, QWidget, QGridLayout, QLabel, QMenu 
from PyQt5.QtCore import Qt 
 
def openFile(): 
     fileName, _ = QFileDialog.getOpenFileName(mainWindow, "Open file", "", "All files (*.*)") 
     if fileName: 
         mainWindow.statusBar().showMessage('User has picked file ' + fileName) 
     else: 
         mainWindow.statusBar().showMessage('User canceled the file dialog.') 
 
def saveFile(): 
     QMessageBox.information(mainWindow, 'Important information', 'Save file has not been implemented yet, sorry!', QMessageBox.Ok) 
 
def toggleLabel(state): 
     if state: 
         label.show() 
     else: 
         label.hide() 
 
app = QApplication(sys.argv) 
 
mainWindow = QMainWindow() 
mainWindow.resize(400,200) 
mainWindow.setWindowTitle("PyQt5 example 2") 
mainWindow.setCentralWidget(QWidget()) 
 
layout = QGridLayout(mainWindow.centralWidget()) 
 
label = QLabel("Some text ...") 
label.setAlignment(Qt.AlignCenter) 
layout.addWidget(label,0,0) 
 
fileMenu = mainWindow.menuBar().addMenu('&File') 
optionsMenu = mainWindow.menuBar().addMenu('&Options') 
 
openAction = QAction('&Open...', mainWindow) 
openAction.triggered.connect(openFile) 
fileMenu.addAction(openAction) 
 
saveAction = QAction('&Save', mainWindow) 
saveAction.triggered.connect(saveFile) 
fileMenu.addAction(saveAction) 
 
exitAction = QAction(app.style().standardIcon(QStyle.SP_DialogCancelButton), '&Exit', mainWindow) 
exitAction.setShortcut('Ctrl+Q') 
exitAction.setStatusTip('Exit application') 
exitAction.triggered.connect(app.quit) 
fileMenu.addAction(exitAction) 
 
toggleLabelAction = QAction('&Toggle label', mainWindow, checkable=True) 
toggleLabelAction.setChecked(True) 
toggleLabelAction.triggered.connect(toggleLabel) 
optionsMenu.addAction(toggleLabelAction) 
 
otherOptionsSubmenu = QMenu('&Other options', mainWindow) 
otherOption1Action = QAction('Other option &1', mainWindow, checkable=True) 
otherOption2Action = QAction('Other option &2', mainWindow, checkable=True) 
 
otherOptionsSubmenu.addAction(otherOption1Action) 
otherOptionsSubmenu.addAction(otherOption2Action) 
optionsMenu.addMenu(otherOptionsSubmenu) 
 
mainWindow.statusBar().showMessage('Waiting for your commands...') 
 
mainWindow.show() 
 
sys.exit(app.exec_()) 
