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

def runGeonamesQuery(query): 
    """query geonames and update list view and web map with results"""
    ui.statusbar.showMessage('Querying GeoNames... please wait!') 
 
    username = ui.geonamesUsernameLE.text()  
    country = ui.geonamesCountryCodeLE.text() if ui.geonamesCountryCodeCB.isChecked() else '' 
    fclass = ui.geonamesFeatureClassLE.text() if ui.geonamesFeatureClassCB.isChecked() else '' 
    limit = ui.geonamesLimitLE.text() 
 
    try: 
        items = core_functions.queryGeonames(query, limit, username, country, fclass ) # run query 
        # create result list from JSON response and store in global variable result 
        global result  
        result  = [(lambda x: {'name': x['toponymName'],'lat': x['lat'], 'lon': x['lng']})(i) for i in items] 
        # update list view and map with results 
        setListViewFromResult(result) 
        mapWV.setHtml(core_functions.webMapFromDictionaryList(result)) 
        ui.statusbar.showMessage('Querying done, ' + str(len(result)) + ' results returned!') 
    except Exception as e: 
        QMessageBox.information(mainWindow, 'Operation failed', 'Querying GeoNames failed with '+ str(e.__class__) + ': ' + str(e), QMessageBox.Ok) 
        ui.statusbar.clearMessage()

def runDirectInput(query): 
    """create single feature and update list view and web map with results"""
    name = ui.directInputNameLE.text() 
    lon = ui.directInputLonLE.text() 
    lat = ui.directInputLatLE.text()  
 
    # create result list with single feature and store in global variable result 
    global result 
    result = [{ 'name': name, 'lat': lat, 'lon': lon }] 
    # update list view and map with results 
    setListViewFromResult(result) 
    mapWV.setHtml(core_functions.webMapFromDictionaryList(result))     
    ui.statusbar.showMessage('Direct input has been added to results list!')

# list view selection functions 
 
def selectAll(): 
    """select all items of the list view widget"""
    for i in range(ui.resultsLV.model().rowCount()): 
        ui.resultsLV.model().item(i).setCheckState(Qt.Checked)  
 
def clearSelection(): 
    """deselect all items of the list view widget"""
    for i in range(ui.resultsLV.model().rowCount()): 
        ui.resultsLV.model().item(i).setCheckState(Qt.Unchecked)  
 
def invertSelection(): 
    """invert current selection of the list view widget"""
    for i in range(ui.resultsLV.model().rowCount()): 
        currentValue = ui.resultsLV.model().item(i).checkState() 
        ui.resultsLV.model().item(i).setCheckState(Qt.Checked if currentValue == Qt.Unchecked else Qt.Unchecked)

# adding features functions 
 
def addFeatures(): 
    """run one of the different functions for adding features based on which tab is currently open"""
    activeTab = ui.addFeaturesTW.currentWidget() 
    addFeaturesHandler[activeTab]() # call a function from the dictionary in addFeatureHandler












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
