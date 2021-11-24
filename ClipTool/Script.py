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

#This function can be used to delete any empty feature class that is generated as the result of clip operation
def deleteIfEmpty(item)
    fcLength = arcpy.GetCount_management(item)        
    if int(fcLength.getOutput(0)) == 0:            
        arcpy.Delete_management(item)

#THis function may be used to check beforehand if a feature class should be put in output layer or not
def intersectLayers():
    bldgFp = os.path.join(wrkingdb, r'bldg_footprints')
    bldgFP_Lyr = arcpy.MakeFeatureLayer_management(bldgFp, "bldgFP_lyr")

    with arcpy.da.SearchCursor(pictBldgFP, ['OBJECTID', 'SHAPE@']) as cur:
        for row in cur:
            curIntersect = arcpy.SelectLayerByLocation_management(bldgFP_Lyr, "INTERSECT", row[1], '', 'NEW_SELECTION')
            intersectCnt = int(arcpy.GetCount_management(curIntersect).getOutput(0))

            if intersectCnt > 0:
                print(f'{row[0]} intersects with {intersectCnt} features')
                

with arcpy.da.SearchCursor(fc, fields) as rows:
    for row in rows:
        arcpy.AddMessage( "Starting Polygon : " + str(row[1]))
        clipper = row[0]
        gdb_name = str(row[1]) + '.gdb'
        
        arcpy.CreateFileGDB_management(output_folder, gdb_name)
        arcpy.env.workspace = input_gdb
        gdb = output_folder + '/' + gdb_name
        rasters = arcpy.ListRasters()
        in_anno = arcpy.ListFeatureClasses('*','Annotation')
        openfc = arcpy.ListFeatureClasses('*','Point')+arcpy.ListFeatureClasses('*','Line')+arcpy.ListFeatureClasses('*','Polygon')+in_anno+rasters
        for fc in openfc:
            copyorclip(gdb,fc)
        
        input_datasets = arcpy.ListDatasets('*', 'Feature')
        rds = arcpy.ListDatasets('*', 'Raster')
        input_datasets.extend(rds)
        for ds in input_datasets:

            fcd = arcpy.Describe(fc)
            sr = fcd.spatialReference
            if ds in rds:
                arcpy.AddMessage(f"Skipping rater dataset {ds}...")
            else:
                out_dataset = arcpy.CreateFeatureDataset_management(gdb, str(ds), sr)
                in_dataset = input_gdb + '/' + str(ds)
                
                arcpy.env.workspace = in_dataset
                rasters = arcpy.ListRasters()
                in_anno = arcpy.ListFeatureClasses('*','Annotation')
                in_feature_class = arcpy.ListFeatureClasses('*','Point')+arcpy.ListFeatureClasses('*','Line')+arcpy.ListFeatureClasses('*','Polygon')+in_anno+rasters
                
                for fc in in_feature_class:
                    
                    copyorclip(out_dataset,fc)
                    

            arcpy.AddMessage("Success...")
del rows

arcpy.AddMessage(" All done !")

#------------------------------------------------------------
a = arcpy.ListDatasets('*', 'Feature')
b = []
for each in a:
    l = str(k)+'\\'+ str(each)
    c = arcpy.Describe(l)
    d = c.spatialReference
    arcpy.env.workspace = l
    m = arcpy.ListFeatureClasses('*')
    b.append((each, d,m) )

print(b)


