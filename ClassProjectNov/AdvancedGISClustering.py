fc = r'D:j\New File Geodatabase.gdb\AgriParclesWIth_Categories'
import numpy as np
ds = arcpy.Describe(fc)
fname = 'CategoryVector'
fields = ['SHAPE@',fname,'OBJECTID_1']

i = 0
vectorList = []
with arcpy.da.SearchCursor(fc, fields) as rows:
    for row in rows:
        if i ==2: break
        arcpy.MakeFeatureLayer_management(fc,'selector')
        
i = 0
vectorList = []
with arcpy.da.SearchCursor(fc, fields) as rows:
    for row in rows:
        i = i+1
        if 'one' in row[1]:
            continue
        else:
            strList = (row[1].replace(' ','').split(','))
            vector =(row[2], [int(x) for x in strList])
            vectorList.append(vector)
            #i = i+1
            j = row[2]

