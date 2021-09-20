import sys 
from PyQt5.QtWidgets import QWidget, QApplication, QLabel 
 
app = QApplication(sys.argv) 
 
window = QWidget() 
window.resize(400,200) 
window.setWindowTitle("PyQt5 example 1") 
 
label = QLabel("Just a window with a label!", window) 
label.move(100,100) 
 
window.show() 
 
sys.exit(app.exec_())
