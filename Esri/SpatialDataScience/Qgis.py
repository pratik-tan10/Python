import os, sys 
import qgis 
import qgis.core
qgis_prefix = os.getenv("QGIS_PREFIX_PATH")      
qgis.core.QgsApplication.setPrefixPath(qgis_prefix, True) 
qgs = qgis.core.QgsApplication([], False)
qgs.initQgis()
layer = qgis.core.QgsVectorLayer('#filepath')
centroidLayer = qgis.core.QgsVectorLayer("Point?crs=" + layer.crs().authid() + "&field=NAME:string(255)", "temporary_points", "memory") 
bufferLayer = qgis.core.QgsVectorLayer("Polygon?crs=" + layer.crs().authid() + "&field=NAME:string(255)", "temporary_buffers", "memory")

centroidProvider = centroidLayer.dataProvider() 
bufferProvider = bufferLayer.dataProvider() 
 
centroidFeatures = []
bufferFeatures = []
