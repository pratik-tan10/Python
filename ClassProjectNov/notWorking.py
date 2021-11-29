import arcpy
import os
import math
fc = arcpy.GetParameterAsText(0) or
#print "a"
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
            print(str(ds))
            gdb = output_folder + '/' + gdb_name
            
            fcd = arcpy.Describe(fc)
            sr = fcd.spatialReference
            out_dataset = arcpy.CreateFeatureDataset_management(gdb, str(ds), sr)
            in_dataset = input_gdb + '/' + str(ds)
            
            arcpy.env.workspace = in_dataset
            
            in_feature_class = arcpy.ListFeatureClasses()
            rasters = arcpy.ListRasters()
            in_anno = arcpy.ListFeatureClasses('*','Annotation')
            in_feature_class = arcpy.ListFeatureClasses()
            try:
                in_feature_class.extend(rasters)
            except: pass
            try:in_feature_class.extend(in_annos)
            except: pass
            for fc in in_feature_class:
                if fc in rasters:
                    try:
                        arcpy.AddMessage("Clipping raster " + str(fc))
                        print("Clipping raster " + str(fc))
                        out_fc = os.path.join(str(out_dataset),str(fc))

                        desc = arcpy.Describe(clipper)

                        xmin = desc.extent.XMin
                        xmax = desc.extent.XMax
                        ymin = desc.extent.YMin
                        ymax = desc.extent.YMax

                        arcpy.Clip_management(fc, "{} {} {} {}".format(xmin, ymin, xmax, ymax), out_fc, clipper, "0", "ClippingGeometry", "MAINTAIN_EXTENT")
                    except: print("error raster")

                elif fc in in_anno:
                    try:
                        out_fc = os.path.join(str(out_dataset),str(fc))
                        arcpy.Project_management(str(fc), out_fc,sr)
                        print("clipping anno "+ str(fc))
                    except Exception as inst:
                        print(type(inst))    # the exception instance
                        print(inst.args)     # arguments stored in .args
                        print(inst)   
                else:
                    try:
                        out_fc = os.path.join(str(out_dataset),str(fc))
                        arcpy.Clip_analysis(str(fc), clipper, out_fc)
                        print("Clipping fc  "+str(fc))
                        #if deleteEmpty: deleteIfEmpty(str(out_fc))
                    except Exception as inst:
                        print(type(inst))    # the exception instance
                        print(inst.args)     # arguments stored in .args
                        print(inst)

                
                '''arcpy.AddMessage("Clipping " + str(fc))
                out_fc = str(out_dataset) + '/' + str(fc)
                arcpy.Clip_analysis(str(fc), clipper, out_fc)'''
                    
            arcpy.AddMessage("Success...")

arcpy.AddMessage(" All done !")
        
