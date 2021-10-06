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
