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

