layers = iface.mapCanvas().layers() 
for layer in layers:
    print(layer)
    print(layer.name())
    print(layer.id())
    print('------')
# If you copy/paste the code - run the part above
# before you run the part below 
# otherwise you'll get a syntax error.
activeLayer = iface.activeLayer()
print('active layer: ' + activeLayer.name())

if activeLayer.type() == QgsMapLayer.VectorLayer: 
    print('This is a vector layer!')

if activeLayer.type() == QgsMapLayer.VectorLayer: 
    if activeLayer.wkbType() == QgsWkbTypes.MultiPolygon: 
        print('This layer contains multi-polygons!')

dir(iface) 
dir(activeLayer)
currentProject = QgsProject.instance() 
print(currentProject.fileName())
currentProject.removeMapLayer(activeLayer.id())
layer = QgsVectorLayer(r'C:\489\TM_WORLD_BORDERS-0.3.shp', 'World borders') 
currentProject.addMapLayer(layer)

renderer = QgsGraduatedSymbolRenderer() 
renderer.setClassAttribute('POP2005') 
layer.setRenderer(renderer) 
layer.renderer().updateClasses(layer, QgsGraduatedSymbolRenderer.Jenks, 5) 
layer.renderer().updateColorRamp(QgsGradientColorRamp(Qt.white, Qt.red)) 
iface.layerTreeView().refreshLayerSymbology(layer.id())
iface.mapCanvas().refreshAllLayers()
