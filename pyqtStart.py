import sys
 
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QPushButton, QHBoxLayout 
from PyQt5.QtCore import Qt 
 
def buttonClickedHandler(c): 
     global counter 
     counter += 1
     label.setText('Thank you for clicking the button ' + str(counter) + ' times!') 
 
app = QApplication(sys.argv) 
 
window = QWidget() 
window.resize(400,200) 
window.setWindowTitle("PyQt5 example 1") 
 
layout = QGridLayout(window) 
 
label = QLabel("Just a window with a label (now perfectly centered!)") 
label.setAlignment(Qt.AlignCenter) 
layout.addWidget(label,0,0) 
 
button = QPushButton("Click me") 
button.setToolTip('This is a <b>QPushButton</b> widget. Click it!') 
 
horLayout = QHBoxLayout() 
horLayout.addStretch(1) 
horLayout.addWidget(button) 
horLayout.addStretch(1) 
layout.addLayout(horLayout,1,0) 
 
button.clicked.connect(buttonClickedHandler) 
 
counter = 0
 
window.show() 
 
sys.exit(app.exec_()) 
