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
        
