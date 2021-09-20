from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton 
 
def convert(): 
    """Takes miles entered, converts them to km, and displays the result"""
    miles = float(entryMiles.text()) 
    entryKm.setText(str(miles * 1.60934)) 
 
app = QApplication([]) 
 
rootWindow = QWidget() 
rootWindow.setWindowTitle("Miles to kilometers") 
rootWindow.resize(500, 200) 
 
gridLayout = QGridLayout(rootWindow) 
 
labelMiles = QLabel('Distance in miles:') 
gridLayout.addWidget(labelMiles, 0, 0) 
 
labelKm = QLabel('Distance in kilometers:') 
gridLayout.addWidget(labelKm, 2, 0) 
 
entryMiles = QLineEdit() 
gridLayout.addWidget(entryMiles, 0, 1) 
 
entryKm = QLineEdit() 
gridLayout.addWidget(entryKm, 2, 1) 
 
convertButton = QPushButton('Convert') 
gridLayout.addWidget(convertButton, 1, 1) 
 
convertButton.clicked.connect(convert) 
 
rootWindow.show() 
 
app.exec_() 
