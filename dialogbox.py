# imports  
 
import sys, random 
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QDialog, \
   QVBoxLayout, QGroupBox, QLabel, QLineEdit, QTextEdit, QHBoxLayout, QListView, QRadioButton, \
   QCheckBox, QComboBox, QDialogButtonBox 
from PyQt5.QtCore import Qt, QVariant 
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem

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
 
mainVerticalLayout = QVBoxLayout(dialogBox) 
 
nameGroupBox = QGroupBox("Name") # row 1 of vertical layout 
mainVerticalLayout.addWidget(nameGroupBox) 
nameGridLayout = QGridLayout(nameGroupBox) 
firstNameLabel = QLabel("First name:") 
nameGridLayout.addWidget(firstNameLabel, 0, 0) 
lastNameLabel = QLabel("Last name:") 
nameGridLayout.addWidget(lastNameLabel, 1, 0) 
firstNameLineEdit = QLineEdit() 
nameGridLayout.addWidget(firstNameLineEdit, 0, 1) 
lastNameLineEdit = QLineEdit() 
nameGridLayout.addWidget(lastNameLineEdit, 1, 1) 
 
imageHorizontalLayout = QHBoxLayout() # row 2 
mainVerticalLayout.addLayout(imageHorizontalLayout) 
imageLabel = QLabel() 
imageLabel.setPixmap(QPixmap("psu.PNG").scaledToWidth(172))  
imageHorizontalLayout.addWidget(imageLabel) 
textEdit = QTextEdit() 
textEdit.setText("<write whatever you want here>") 
imageHorizontalLayout.addWidget(textEdit) 
   
listGridLayout = QGridLayout() # row 3 
mainVerticalLayout.addLayout(listGridLayout) 
listView = QListView() 
listGridLayout.addWidget(listView, 0, 0, 4, 1) 
clearPushButton = QPushButton("Clear") 
listGridLayout.addWidget(clearPushButton, 0, 1) 
hidePushButton = QPushButton("Hide") 
listGridLayout.addWidget(hidePushButton, 1, 1) 
showPushButton = QPushButton("Show") 
listGridLayout.addWidget(showPushButton, 2, 1) 
listWordsPushButton = QPushButton("List words") 
listGridLayout.addWidget(listWordsPushButton, 3, 1) 
           
widgetGroupBox = QGroupBox() # row 4 
mainVerticalLayout.addWidget(widgetGroupBox) 
widgetGridLayout = QGridLayout(widgetGroupBox) 
greatRadioButton = QRadioButton("I think this dialog box is great!") 
greatRadioButton.setChecked(True) 
widgetGridLayout.addWidget(greatRadioButton, 0, 0) 
neutralRadioButton = QRadioButton("I am neutral towards this dialog box!") 
widgetGridLayout.addWidget(neutralRadioButton, 1, 0) 
horribleRadioButton = QRadioButton("This dialog box is just horrible!") 
widgetGridLayout.addWidget(horribleRadioButton, 2, 0) 
checkBox = QCheckBox("Check me out") 
widgetGridLayout.addWidget(checkBox, 0, 1)  
comboBox = QComboBox() 
widgetGridLayout.addWidget(comboBox, 0, 2) 
widgetPushButton = QPushButton("I am a push button spanning two columns") 
widgetGridLayout.addWidget(widgetPushButton, 2, 1, 1, 2) 
  
buttonBox = QDialogButtonBox() # row 5 
buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok) 
mainVerticalLayout.addWidget(buttonBox)

# functions for interactions
def populateListView(): 
     words = textEdit.toPlainText().split() 
     m = QStandardItemModel() 
     for w in words: 
         item = QStandardItem(w) 
         item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled) 
         item.setData(QVariant(Qt.Checked), Qt.CheckStateRole) 
         m.appendRow(item) 
     listView.setModel(m) 
 
def populateComboBoxWithRandomNumbers(): 
     comboBox.clear() 
     for i in range(5): 
         comboBox.addItem(str(random.randrange(10)))

# functions for modal version 
 
# functions for modeless version 
 
# connect signals and other initializations 
 
button.clicked.connect(dialogBox.exec_) # invoke dialog modal version 
 
# run the program 
  
mainWindow.show() 
 
sys.exit(app.exec_()) 
