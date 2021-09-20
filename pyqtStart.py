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
 
layout = QGridLayout(window)
label = QLabel("Just a window with a label!", window) 
label.setAlignment(Qt.AlignCenter) 
layout.addWidget(label,0,0)

button = QPushButton("Close me") 
button.setToolTip('This is a <b>QPushButton</b> widget. Clicking it will close the program!') 
layout.addWidget(button,1,0) 
 
button.clicked.connect(app.quit) 
 
window.show() 
 
sys.exit(app.exec_())
