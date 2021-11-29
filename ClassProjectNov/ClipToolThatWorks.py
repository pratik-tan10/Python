import arcpy
import os
import math
fc = arcpy.GetParameterAsText(0)
input_gdb =arcpy.GetParameterAsText(2)
#print "b.."
output_folder =  arcpy.GetParameterAsText(3)
#print "c...."
prj_file = arcpy.GetParameterAsText(4)
#sr = arcpy.SpatialReference(prj_file)
i = 1
arcpy.AddMessage(str(i) + "Lets Begin...")
fields = ['SHAPE@','SHEETNO']
nameField = arcpy.GetParameterAsText(1)
#fields.extend(nameField)
with arcpy.da.SearchCursor(fc, fields) as rows:
    for row in rows:
        arcpy.AddMessage( "Starting Sheet : " + str(row[1]))
        clipper = row[0]
        gdb_name = str(row[1]) + '.gdb'
        arcpy.CreateFileGDB_management(output_folder, gdb_name)
        arcpy.env.workspace = input_gdb
        feature_class=row[0]
        area_of_interest= feature_class
        outputlayer=str(row[1])       
        input_datasets = arcpy.ListDatasets('*', 'Feature')
        for ds in input_datasets:
            
            print(str(ds).lower())
            gdb = output_folder + '/' + gdb_name
            if str(ds) == "ADMIN_LAYER":
                continue
            else:
                fcd = arcpy.Describe(fc)
                sr = fcd.spatialReference
                out_dataset = arcpy.CreateFeatureDataset_management(gdb, str(ds), sr)
                in_dataset = input_gdb + '/' + str(ds)
                
                arcpy.env.workspace = in_dataset
                in_feature_class = arcpy.ListFeatureClasses()
                for fc in in_feature_class:
                    arcpy.AddMessage("Clipping " + str(fc))
                    out_fc = str(out_dataset) + '/' + str(fc)
                    arcpy.Clip_analysis(str(fc), clipper, out_fc)
        
            arcpy.AddMessage("Success...")

arcpy.AddMessage(" All done !")
        
