from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton 
 
class ConverterWidget(QWidget): 
 
    def __init__(self): 
        super(ConverterWidget,self).__init__() 
 
        self.setWindowTitle("Miles to kilometers") 
        self.resize(500, 200) 
 
        self.gridLayout = QGridLayout(self) 
 
        self.labelMiles = QLabel('Distance in miles:') 
        self.gridLayout.addWidget(self.labelMiles, 0, 0) 
 
        self.labelKm = QLabel('Distance in kilometers:') 
        self.gridLayout.addWidget(self.labelKm, 2, 0) 
 
        self.entryMiles = QLineEdit() 
        self.gridLayout.addWidget(self.entryMiles, 0, 1) 
 
        self.entryKm = QLineEdit() 
        self.gridLayout.addWidget(self.entryKm, 2, 1) 
 
        self.convertButton = QPushButton('Convert') 
        self.gridLayout.addWidget(self.convertButton, 1, 1) 
 
        self.convertButton.clicked.connect(self.convert) 
 
    def convert(self): 
         miles = float(self.entryMiles.text()) 
         self.entryKm.setText(str(miles * 1.60934)) 
 
app = QApplication([]) 
converter = ConverterWidget() 
 
converter.show() 
app.exec_() 
