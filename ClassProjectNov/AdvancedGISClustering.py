fc = r'D:j\New File Geodatabase.gdb\AgriParclesWIth_Categories'
import numpy as np
ds = arcpy.Describe(fc)
fname = 'CategoryVector'
fields = ['SHAPE@',fname,'OBJECTID_1']

