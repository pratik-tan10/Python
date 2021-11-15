'''This script takes as input a Digital Elevation model (dem) and
produces a raster showing sum of area of each cell to upstream to it.
Other intermediate files are created only for temporary and are not saved to disk '''
#Imports and setup
import arcpy
from arcpy import env
from arcpy.sa import *

#Check Spatial Analyst Extension in ArcGIS
arcpy.CheckOutExtension("Spatial")


#Input Elevation file
dem = arcpy.GetParameterAsText(0)

#Describe input dem file to get working directory
desc = arcpy.Describe(dem)

#Set Workspace
env.workspace = desc.path
#Set override to true
env.overwriteOutput = True

#Output file name
outfilename = arcpy.GetParameterAsText(1)

#Prints to conosole that process has started
arcpy.AddMessage("Process Begins...")
#fill the input dem to remove sinkholes
filled = Fill(dem)

#Compute flow direction
flowdir = FlowDirection(filled)

#Compute flow accumulation
flowacc = FlowAccumulation(flowdir)

#Describe a raster object to get it's x and y cell size/resolution
ras = arcpy.Describe(dem)
x_size = ras.meanCellWidth
y_size = ras.meanCellHeight

#compute area of one cell
cell_size = x_size*y_size

#Compute drainage by muliplying flow accumulation with area of one cell
drainage = Times(flowacc,cell_size)

#Save output raster to disk
drainage.save(outfilename)

#Prints to console that process had successfully ended
arcpy.AddMessage(f"Done!\nPlease check the file:\t{arcpy.Describe(outfilename).file}\nIn the following directory\n{env.workspace}")

#If not a single user GIS, please uncomment the following line to uncheck Spatial analyst extension
#arcpy.CheckInExtension("Spatial")
