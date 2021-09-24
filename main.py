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
# query and direct input functions 
 
def runQuery(): 
    """run one of the different query services based on which tab is currently open"""
    queryString = ui.queryTermLE.text() 
    activeTab = ui.queryServicesTW.currentWidget() 
    queryHandler[activeTab](queryString)   # call a function from the dictionary in queryHandler

def setListViewFromResult(r): 
    """populate list view with checkable entries created from result list in r"""
    m = QStandardItemModel() 
    for item in r: 
        item = QStandardItem(item['name'] + ' ('+item['lat'] + ',' + item['lon'] + ')') 
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled) 
        item.setData(QVariant(Qt.Checked), Qt.CheckStateRole) 
        m.appendRow(item) 
    ui.resultsLV.setModel(m)
def runNominatimQuery(query): 
    """query nominatim and update list view and web map with results"""
    ui.statusbar.showMessage('Querying Nominatim... please wait!') 
 
    country = ui.nominatimCountryCodeLE.text() if ui.nominatimCountryCodeCB.isChecked() else '' 
    limit = ui.nominatimLimitLE.text()  
 
    try: 
        items = core_functions.queryNominatim(query, limit, country) # run query 
        # create result list from JSON response and store in global variable result 
        global result  
        result = [(lambda x: {'name': x['display_name'],'lat': x['lat'], 'lon': x['lon']})(i) for i in items] 
        # update list view and map with results 
        setListViewFromResult(result) 
        mapWV.setHtml(core_functions.webMapFromDictionaryList(result))       
        ui.statusbar.showMessage('Querying done, ' + str(len(result)) + ' results returned!') 
    except Exception as e: 
        QMessageBox.information(mainWindow, 'Operation failed', 'Querying Nominatim failed with '+ str(e.__class__) + ': ' + str(e), QMessageBox.Ok ) 
        ui.statusbar.clearMessage()














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
arcpyAvailable = core_functions.importArcpyIfAvailable() 
 
if not arcpyAvailable: 
    ui.addFeaturesTW.setCurrentWidget(ui.csvTab) 
    ui.addFeaturesTW.setTabEnabled(ui.addFeaturesTW.indexOf(ui.shapefileTab),False) 
    ui.addFeaturesTW.setTabEnabled(ui.addFeaturesTW.indexOf(ui.layerTab),False) 
    ui.statusbar.showMessage('arcpy not available. Adding to shapefiles and layers has been disabled.') 
else: 
    import arcpy 
    if core_functions.runningAsScriptTool(): 
        runningAsScriptTool = True
        updateLayers() 
    else: 
        ui.addFeaturesTW.setTabEnabled(ui.addFeaturesTW.indexOf(ui.layerTab),False) 
        ui.statusbar.showMessage(ui.statusbar.currentMessage() + 'Not running as a script tool. Adding to layer has been disabled.')
#======================================= 
# run app 
#======================================= 
mainWindow.show() 
sys.exit(app.exec_()) 