from arcgis.gis import GIS
gis = GIS()
from arcgis.gis import GIS
gis = GIS('https://www.arcgis.com', '<your username>', '<your password>')
gis?

import os,sys
os.environ["PATH"] = r"{};{}".format(os.environ["PATH"], r"C:\Program Files\ArcGIS\Pro\bin")
sys.path.append(r"C:\Program Files\ArcGIS\Pro\Resources\ArcPy")
import arcgis
from arcgis.gis import GIS
gis = GIS('pro')
gis?

#Access User Properties
user = gis.users.get('<your username>')
user
user.email
user.fullName

