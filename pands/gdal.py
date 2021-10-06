from osgeo import gdal
from osgeo import ogr
froom osgeo import osr

shapefile = r'C:\489\L3\TM_WORLD_BORDERS-0.3.shp'
drv =ogr.GetDriverByName('ESRI Shapefile')
dataSet = drv.Open(shapefile)

layer = dataSet.GetLayer(0)
layerDefinition = layer.GetLayerDefn()
for i in range(layerDefinition.GetFieldCount()):
    print(layerDefinition.GetFieldDefn(i).GetName())

for feature in layer:
    print(feature.GetField('NAME'))
layer.ResetReading()

for feature in layer:
    print(feature.GetField('NAME') + '–' + feature.GetGeometryRef().Centroid().ExportToWkt())
layer.ResetReading()

layer.SetAttributeFilter('POP2005 > 100000000')
for feature in layer:
    print(feature.GetField('NAME'))
layer.ResetReading()

