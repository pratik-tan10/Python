#Necessary imports
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime as dt

import arcgis
import arcgis.geoanalytics
from arcgis.gis import GIS

from arcgis.geoanalytics.summarize_data import aggregate_points, describe_dataset
from arcgis.geoanalytics.analyze_patterns import calculate_density, find_hot_spots
from arcgis.geoanalytics.manage_data import clip_layer, run_python_script

#Connecting to GIS
gis = GIS('https://pythonapi.playground.esri.com/portal', 'arcgis_python', 'amazing_arcgis_123')

#Check if GeoAnalytics is supported
arcgis.geoanalytics.is_supported()

#Create big data file share

bigdata_datastore_manager = arcgis.geoanalytics.get_datastores()
bigdata_datastore_manager


bigdata_fileshares = bigdata_datastore_manager.search(id='cff51a1a-4f27-4955-a3ef-5fa23240ccf9')
bigdata_fileshares

file_share_folder = bigdata_fileshares[0]

#manifest describes schema
manifest = file_share_folder.manifest
manifest
manifest['datasets'][0]['geometry']['spatialReference'] = { "wkid": 102682, "latestWkid": 3452 }
file_share_folder.manifest = manifest
file_share_folder.manifest

#search for big dat file shares
search_result = gis.content.search("bigDataFileShares_ServiceCallsOrleans", item_type = "big data file share", max_items=40)
search_result

data_item = search_result[0]
data_item

calls = data_item.layers[0]
calls.properties
block_grp_item = gis.content.get('9975b4dd3ca24d4bbe6177b85f9da7bb')
block_grp_item
blk_grp_lyr = block_grp_item.layers[0]



