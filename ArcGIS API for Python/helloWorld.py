from arcgis.gis import GIS
gis = GIS('home')

gis = GIS()
gis?
:
user = gis.users.get('john.smith')
user
user['firstName']
user.lastName

map1 = gis.map("Palm Springs, CA")
map1

from IPython.display import display

items = gis.content.search('Palm Springs Trails')
for item in items:
    display(item)
    

# Let us filter out the item with title 'Trails' that we want to add
item_to_add = [temp_item for temp_item in items if temp_item.title == "Trails"]
map1.add_layer(item_to_add[0])
