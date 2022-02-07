import arcpy,os

InFolder = arcpy.GetParameterAsText(0)
Dest=arcpy.GetParameterAsText(1)

arcpy.env.workspace=InFolder
#The raster datasets in the input workspace
in_raster_datasets = arcpy.ListRasters()

arcpy.CreateFeatureclass_management(os.path.dirname(Dest),
                                   os.path.basename(Dest),
                                   "POLYGON")
arcpy.AddField_management(Dest,"RasterName", "String","","",250)
arcpy.AddField_management(Dest,"RasterPath", "String","","",250)

cursor = arcpy.InsertCursor(Dest)
point = arcpy.Point()
array = arcpy.Array()
corners = ["lowerLeft", "lowerRight", "upperRight", "upperLeft"]
  
for Ras in in_raster_datasets:
    feat = cursor.newRow()  
    r = arcpy.Raster(Ras)
    for corner in corners:    
        point.X = getattr(r.extent, "%s" % corner).X
        point.Y = getattr(r.extent, "%s" % corner).Y
        array.add(point)
    array.add(array.getObject(0))
    polygon = arcpy.Polygon(array)
    feat.shape = polygon
    feat.setValue("RasterName", Ras)
    feat.setValue("RasterPath", InFolder + "\\" + Ras)
    cursor.insertRow(feat)
    array.removeAll()
del feat
del cursor
