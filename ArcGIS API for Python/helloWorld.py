from arcgis.gis import GIS
gis = GIS('home')

gis = GIS()
gis?
:
user = gis.users.get('john.smith')
user
user['firstName']
user.lastName

