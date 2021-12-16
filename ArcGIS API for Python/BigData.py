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


file_share_folder = bigdata_fileshares[0]

#manifest describes schema

#search for big dat file shares

#describe data

#clip to a boundary

#summarize data
#finding hot spots and cold spots

