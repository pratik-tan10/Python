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

#Create Map
map = gis.map('State College, PA')
map

#set Zoom
map.zoom = 11
#Change basemap to satellite image
map.basemap = 'satellite'

#Add marker on map
from arcgis.geocoding import geocode
walker = geocode('Walker Bldg, State College, PA')[0]
oldMain = geocode('Old Main Bldg, State College, PA')[0]
map.draw(walker, {'title':'Walker Bldg', 'content': walker['attributes']['LongLabel']})
map.draw(oldMain, {'title':'Old Main Bldg', 'content': oldMain['attributes']['LongLabel']})

#Draw Freehand line between those two points
from arcgis.geometry import lengths
 
def calcLength(map,g):
    l = lengths(g['spatialReference'], [g], '', 'geodesic')
    print('Length: '+ str(l[0]) + 'm.')


