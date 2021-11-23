#imports
from arcpy import env
import arcpy
import math
import os


fc = arcpy.GetParameterAsText(0)
input_gdb =arcpy.GetParameterAsText(1)
nameField = arcpy.GetParameterAsText(2) or 'SHEETNO'
output_folder =  arcpy.GetParameterAsText(3)
i=0
arcpy.AddMessage(f"{i} Lets Begin...")
fields = ['SHAPE@',nameField]

def copyorclip(outl,fc):
    if fc not in in_anno and fc not in rasters:
        arcpy.AddMessage("Clipping " + str(fc))
        out_fc = str(out_dataset) + '/' + str(fc)
        arcpy.Clip_analysis(str(fc), clipper, out_fc)
    elif fc in in_anno:
        arcpy.AddMessage("Copying " + str(fc))
        out_fc = str(out_dataset) + '/' + str(fc)
        arcpy.Copy_management(str(fc), out_fc)
    else:
        arcpy.AddMessage("Clipping raster " + str(fc))
        out_fc = str(out_dataset) + '/' + str(fc)

        desc = arcpy.Describe(clipper)

        xmin = desc.extent.XMin
        xmax = desc.extent.XMax
        ymin = desc.extent.YMin
        ymax = desc.extent.YMax

        arcpy.Clip_management(fc, f"{xmin} {ymin} {xmax} {ymax}", out_fc, clipper, "0", "ClippingGeometry", "MAINTAIN_EXTENT")

with arcpy.da.SearchCursor(fc, fields) as rows:
    for row in rows:
        arcpy.AddMessage( "Starting Polygon : " + str(row[1]))
        clipper = row[0]
        
        #set gdb name
        if (row[1][0]).isalpha():
            gdb_name = str(row[1]) + '.gdb'
        else:
            gdb_name = 'o'+str(row[1]) + '.gdb'
        
        arcpy.CreateFileGDB_management(output_folder, gdb_name)
        arcpy.env.workspace = input_gdb
        gdb = output_folder + '/' + gdb_name
        rasters = arcpy.ListRasters()
        in_anno = arcpy.ListFeatureClasses('*','Annotation')
        openfc = arcpy.ListFeatureClasses('*','Point')+arcpy.ListFeatureClasses('*','Line')+arcpy.ListFeatureClasses('*','Polygon')+in_anno+rasters
        for fc in openfc:
            copyorclip(gdb,fc)
        
        
