import sys 
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

from PyQt5.QtCore import Qt, QCoreApplication
 
app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
 
app.aboutToQuit.connect(app.deleteLater) 
window = QWidget() 
window.resize(400,200) 
window.setWindowTitle("PyQt5 example 1") 
 
label = QLabel("Just a window with a label!", window) 
label.move(100,100) 
 
window.show() 
 
sys.exit(app.exec_())
