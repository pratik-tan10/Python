import sys, csv 
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyle, QFileDialog, QDialog, QMessageBox, QSizePolicy 
from PyQt5.QtGui import QStandardItemModel, QStandardItem,  QDoubleValidator, QIntValidator 
from PyQt5.QtCore import QVariant 
from PyQt5.Qt import Qt
 
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView as WebMapWidget
except:
    from PyQt5.QtWebKitWidgets import QWebView as WebMapWidget
 
import gui_main  
import gui_newshapefile 
import core_functions 
 
# ======================================= 
# GUI event handler and related functions 
# ======================================= 
 
#========================================== 
# create app and main window + dialog GUI 
# =========================================  
app = QApplication(sys.argv) 
 
# set up main window 
mainWindow = QMainWindow() 
ui = gui_main.Ui_MainWindow() 
ui.setupUi(mainWindow) 
 
ui.actionExit.setIcon(app.style().standardIcon(QStyle.SP_DialogCancelButton)) 
ui.layerRefreshTB.setIcon(app.style().standardIcon(QStyle.SP_BrowserReload)) 
 
ui.directInputLatLE.setValidator(QDoubleValidator()) 
ui.directInputLonLE.setValidator(QDoubleValidator()) 
ui.nominatimLimitLE.setValidator(QIntValidator()) 
ui.geonamesLimitLE.setValidator(QIntValidator()) 
 
mapWV = WebMapWidget() 
mapWV.page().profile().setHttpAcceptLanguage("en-US")
mapWV.setHtml(core_functions.webMapFromDictionaryList([])) 
ui.resultsListAndMapHBL.addWidget(mapWV) 
mapWV.setFixedSize(300,200) 
mapWV.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)) 
 
# set up new shapefile dialog 
createShapefileDialog = QDialog(mainWindow) 
createShapefileDialog_ui = gui_newshapefile.Ui_Dialog() 
createShapefileDialog_ui.setupUi(createShapefileDialog) 

#========================================== 
# connect signals 
#========================================== 
 
#================================== 
# initialize global variables 
#================================== 
# dictionary mapping tabs from services tab widget to event handler functions 
queryHandler = { ui.nominatimTab: runNominatimQuery, ui.geonamesTab: runGeonamesQuery, ui.directInputTab: runDirectInput } 
 
# dictionary mapping tabs from add feature tab widget to event handler functions 
addFeaturesHandler = { ui.layerTab: addFeaturesToLayer, ui.shapefileTab: addFeaturesToShapefile, ui.csvTab: addFeaturesToCSV } 
 
result = []                     # global variable for storing query results as list of dictionaries 
arcValidLayers= {}              # dictionary mapping layer names to layer objects       
 
arcpyAvailable = False          # indicates whether is available for import 
runningAsScriptTool = False     # indicates whether script is run as script tool inside ArcGIS 

#============================================ 
# test availability and if run as script tool 
#============================================ 
 
#======================================= 
# run app 
#======================================= 
mainWindow.show() 
sys.exit(app.exec_()) 
