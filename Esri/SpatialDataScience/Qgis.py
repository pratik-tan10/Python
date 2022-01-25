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

areaPolygon = qgis.core.QgsGeometry.fromWkt('POLYGON ( (6.3 -14, 52 -14, 52 -40, 6.3 -40, 6.3 -14) )')
for feature in layer.getFeatures(): 
    if feature.geometry().intersects(areaPolygon): 
        centroid = qgis.core.QgsFeature() 
        centroid.setAttributes([feature['NAME']]) 
        centroid.setGeometry(feature.geometry().centroid()) 
        centroidFeatures.append(centroid) 
 
        buffer = qgis.core.QgsFeature() 
        buffer.setAttributes([feature['NAME']]) 
        buffer.setGeometry(feature.geometry().centroid().buffer(2.0,100)) 
        bufferFeatures.append(buffer)
     
centroidProvider.addFeatures(centroidFeatures) 
bufferProvider.addFeatures(bufferFeatures)
qgis.core.QgsVectorFileWriter.writeAsVectorFormat(centroidLayer, r'C:\489\centroids.gpkg', "utf-8", layer.crs(), "GPKG") 
qgis.core.QgsVectorFileWriter.writeAsVectorFormat(bufferLayer, r'C:\489\buffers.gpkg', "utf-8", layer.crs(), "GPKG")
qgs.exitQgis()

