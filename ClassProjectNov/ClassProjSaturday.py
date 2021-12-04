from datetime import datetime
import arcpy
import os
#import math

fc = arcpy.GetParameterAsText(0)

input_gdb =arcpy.GetParameterAsText(1)

output_folder =  arcpy.GetParameterAsText(2) or r'C:\Users\Research Lab\Desktop\Pratik\GY539\xnc'

#prj_file = arcpy.GetParameterAsText(3) or r'D:\Pythoning\Nepal_Nagarkot_TM_84.prj'
#xmlFile = arcpy.GetParameterAsText(4) or r'D:\Pythoning\Nagarkot25000TM84GridGraticule.xml'
#fc_gcs = arcpy.GetParameterAsText(3)
nameField = arcpy.GetParameterAsText(3)
DIE = arcpy.GetParameter(4)

arcpy.AddMessage(f" DIE: {DIE}, type: {type(DIE)}")
#sr = arcpy.SpatialReference(prj_file)
i = 1
arcpy.AddMessage(str(i) + "Lets Begin...")
fields = ['SHAPE@',str(nameField)]
pname =  'log'+"_" + str(datetime.now())+'.txt'
cname = pname.replace(':','_')
cleanName = cname.replace(' ','_')

outfname=os.path.join(output_folder,cleanName)
arcpy.AddMessage(f" Fielename: {outfname}")
if os.path.exists(outfname):
    os.remove(outfname)
def writeMessage(message):
    with open(outfname,'a') as of:
        of.writelines(str(message) +" : " + str(datetime.now())+'\n')

def deleteIfEmpty(item):
    fcLength = arcpy.GetCount_management(item)        
    if int(fcLength.getOutput(0)) == 0:            
        arcpy.Delete_management(item)
        arcpy.AddMessage(f"features: {fcLength.getOutput(0)} so deleting {item}")
        writeMessage(f"features: {fcLength.getOutput(0)} so deleting {item}")

with arcpy.da.SearchCursor(fc, fields) as rows:
    for row in rows:
        arcpy.AddMessage( "Starting Sheet : " + str(row[1]))
        writeMessage( "Starting Sheet : " + str(row[1]))
        clipper = row[0]
        gdb_name = str(row[1]) + '.gdb'
        #xml_name= "Nagarkot25000TM81GridGraticule"+".xml"
        arcpy.CreateFileGDB_management(output_folder, gdb_name)
        arcpy.env.workspace = input_gdb
        
        input_datasets = arcpy.ListDatasets('*', 'Feature')
        for ds in input_datasets:
            arcpy.AddMessage("Starting " + str(ds))
            print( str(ds).lower())
            gdb = os.path.join(output_folder, gdb_name)
            dsn = os.path.join(input_gdb, str(ds))
            try:
                fcd = arcpy.Describe(ds)
                sr = fcd.spatialReference
                print("from ds only.")
            except:
                sr = arcpy.Describe(dsn).spatialReference
                print('From dsn')
            
            
            out_dataset = arcpy.CreateFeatureDataset_management(gdb, str(ds), sr)
            in_dataset = os.path.join(input_gdb,str(ds))
            
            arcpy.env.workspace = in_dataset
            in_feature_class = arcpy.ListFeatureClasses()
            for fc in in_feature_class:
                arcpy.AddMessage("Clipping " + str(fc))
                writeMessage("Clipping " + str(fc))
                out_fc = os.path.join(str(out_dataset), str(fc))
                arcpy.Clip_analysis(str(fc), clipper, out_fc)
                if DIE: deleteIfEmpty(out_fc)
                
                #arcpy.AddMessage("Copying " + str(fc))
			#in_fc = str(fc)
                        #out_fc = str(out_dataset) + '/' + str(fc)
                        #arcpy.Copy_management(in_fc, out_fc)
            
                 
            arcpy.AddMessage("Success...")
del rows

arcpy.AddMessage(" All done !")
        
