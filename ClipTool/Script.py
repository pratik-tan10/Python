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

