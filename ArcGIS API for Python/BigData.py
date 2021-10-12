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

#describe data
description = describe_dataset(input_layer=calls,
                               extent_output=True,
                               sample_size=1000,
                               output_name="Description of service calls" + str(dt.now().microsecond),
                               return_tuple=True)

description.output_json
description.sample_layer
description.sample_layer.query().sdf

m1 = gis.map()
m1
m1.add_layer(description.sample_layer)

#clip to a boundary
clip_result = clip_layer(calls, blk_grp_lyr, output_name="service calls in new Orleans" + str(dt.now().microsecond))

orleans_calls = clip_result.layers[0]
m2 = gis.map('New Orleans')
m2
m2.add_layer(orleans_calls)

#summarize data
arcgis.env.prcess_spatial_reference = 54034
agg_result = aggregate_points(orleans_calls, polygon_layer = blk_grp_lyr, output_name = "aggregate results of call" +str(dt.now().microsecond))

agg_result

m3 = gis.map()
m3
m3.add_layer(agg_result)
m3.legend=True


