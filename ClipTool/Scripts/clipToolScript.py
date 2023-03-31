'''This script takes following inputs:
    ->fc, which is a polygon featureclass that is used to clip a database
    ->input_gdb, which is a large gdb to be clipped to smaller gdbs
    ->output_folder, which is where the newly created smaller gdbs are stored
    ->nameField, it is the field with unique values which will be used to name the output smaller gdbs
    ->DIE, it is a boolean which asks if empty featureclasses in output should be deleted or not
    ->prj_file, it is a .prj  file of co-ordinate reference system, to which user wants to 
        output gdbs to be. It is an optional parameter. If not valid file is found, the CRS of input
        datasets will be used in output datasets.
'''
#Import libraries
from datetime import datetime
import arcpy
import os

#Setup User inputs
fc = arcpy.GetParameterAsText(0)

input_gdb =arcpy.GetParameterAsText(1)

output_folder =  arcpy.GetParameterAsText(2)

nameField = arcpy.GetParameterAsText(3)
DIE = arcpy.GetParameter(4)
prj_file = arcpy.GetParameterAsText(5)

#chk() function checks if user wants to enforce different projection to output
def chk():
    if prj_file:
        return prj_file
    else: return 'same as input'
    
fileNameraw =  'log'+"_" + str(datetime.now())+'.txt'
cname = fileNameraw.replace(':','_')#removes unwanted characters from fileNameraw
cleanName = cname.replace(' ','_')#Further removes whitespaces from filename of log file

#Define full path of logfile
outfname = os.path.join(output_folder,cleanName)

#If the file already exists, it is deleted
if os.path.exists(outfname):
    os.remove(outfname)

#writeMessage function takes a message string, outputs ints to tool console
#and also writes to log file along with a timestamp of the event
def writeMessage(message):
    arcpy.AddMessage(str(message))
    with open(outfname,'a') as of:
        of.writelines(str(message) +" @ " + str(datetime.now())+'\n')
#writeM simply displays message to the console
#and writes that message to log file without timestamp
def writeM(message):
    arcpy.AddMessage(str(message))
    with open(outfname,'a') as of:
        of.writelines(str(message)+'\n')

#Writes and prints to tool console the input parameters used
writeM("Inputs Files\n")
writeM(f"Input Cipper Polygon: {fc}\t")
writeM(f"Input Database: {input_gdb}\t")
writeM(f"Output Folder: {output_folder}\t")
writeM(f"Output CRS: {chk()}\t")
writeM(f"Delete Empty Feature Classes: {DIE}, type: {type(DIE)}")
writeM('\n')
#Process starts
writeMessage("Process started at: ")
fields = ['SHAPE@',str(nameField)]

#deleteIfEmpty function checks if a featureclass is empty or not, then deletes it if it is empty
def deleteIfEmpty(item):
    fcLength = arcpy.GetCount_management(item)        
    if int(fcLength.getOutput(0)) == 0:            
        arcpy.Delete_management(item)
        writeMessage(f"features: {fcLength.getOutput(0)} so deleting {item}")
        
#projectDbase function projects the input gdb to match user defined CRS
#It is only called if user provides a projection file
def projectDbase():
    xr = r"..\Scratch"
    writeMessage(f"Scratch Workspace location: {os.path.abspath(xr)}")
    try:
        outCS = arcpy.SpatialReference(prj_file)
        arcpy.env.workspace = input_gdb
        arcpy.CreateFileGDB_management(xr, 'scratch.gdb')
        inds = arcpy.ListDatasets('*', 'Feature')
        for ind in inds:
            writeMessage(f"Projecting {str(ind)}")
            ogd = os.path.join(xr, 'scratch.gdb')
            oupd = os.path.join(ogd,str(ind))
            arcpy.Project_management(ind, oupd, outCS)
        return str(os.path.join(xr, 'scratch.gdb'))
    except:
        writeM("Failed : Tried to enforce wrong Coordinate system. Retaining the CRS of Input GDB.")
        return input_gdb

#If user provides a projection file, the projectDbase function is called
#and the output of that function is used as input gdb
if prj_file:
    input_gdb = projectDbase()
    arcpy.AddMessage(str(input_gdb))

#this is the main operation
with arcpy.da.SearchCursor(fc, fields) as rows:
    for row in rows:
        writeMessage( "\nStarting Polygon : " + str(row[1]))
        clipper = row[0]
        gdb_name = str(row[1]) + '.gdb'
        arcpy.CreateFileGDB_management(output_folder, gdb_name)
        arcpy.env.workspace = input_gdb
        
        input_datasets = arcpy.ListDatasets('*', 'Feature')
        for ds in input_datasets:
            writeM("Starting " + str(ds))
            print( str(ds).lower())
            gdb = os.path.join(output_folder, gdb_name)
            
            #grabs the crs of input dataset
            dsn = os.path.join(input_gdb, str(ds))
            try:
                fcd = arcpy.Describe(ds)
                sr = fcd.spatialReference
            except:
                sr = arcpy.Describe(dsn).spatialReference
            
            #dataset from input gdb is creted to output gdb
            out_dataset = arcpy.CreateFeatureDataset_management(gdb, str(ds), sr)
            in_dataset = os.path.join(input_gdb,str(ds))
            
            #dataset from input gdb is set as workspace to list its feature classes
            arcpy.env.workspace = in_dataset
            in_feature_class = arcpy.ListFeatureClasses()
            for fc in in_feature_class:
                try:
                    writeMessage("Clipping " + str(fc))
                    out_fc = os.path.join(str(out_dataset), str(fc))
                    #clips the feature class from input database and outputs to output database
                    arcpy.Clip_analysis(str(fc), clipper, out_fc)
                    #if DIE is true, for the recently created output, checks if it should be deleted
                    if DIE: deleteIfEmpty(out_fc)
                except: continue
                 
del rows

writeMessage("\n\nAll done !")