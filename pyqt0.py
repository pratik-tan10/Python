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
  
