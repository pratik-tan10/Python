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

