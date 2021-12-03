!conda create -n gee python=3.8
!conda activate gee
!conda install geopandas
!conda install mamba -c conda-forge
!mamba install geemap -c conda-forge

#imports
import os
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
pkgs = ['geemap', 'leafmap', 'geopandas']
if "google.colab" in sys.modules:
    for pkg in pkgs:
        install(pkg)

import os
import ee
import geemap

Map = geemap.Map() 
Map
Map = geemap.Map(center=(40, -100), zoom=4, lite_mode=True) 
Map
Map = geemap.Map()
Map.add_basemap('HYBRID')
Map

from geemap.basemaps import basemaps
Map.add_basemap(basemaps.OpenTopoMap)
Map = geemap.Map()
Map
Map = geemap.Map()

url = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}'
Map.add_tile_layer(url, name='Google Terrain', attribution='Google')
Map
naip_url = 'https://services.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?'
Map.add_wms_layer(url=naip_url, layers='0', name='NAIP Imagery', format='image/png', shown=True)

Map = geemap.Map()
Map

js_snippet = """
// Load an image.
var image = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_044034_20140318');

// Define the visualization parameters.
var vizParams = {
  bands: ['B5', 'B4', 'B3'],
  min: 0,
  max: 0.5,
  gamma: [0.95, 1.1, 1]
};

// Center the map and display the image.
Map.setCenter(-122.1899, 37.5010, 10); // San Francisco Bay
Map.addLayer(image, vizParams, 'false color composite');

"""
geemap.js_snippet_to_py(js_snippet, add_new_cell=True, import_ee=True, import_geemap=True, show_map=True)

import ee
import geemap

Map = geemap.Map()

# Load an image.
image = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_044034_20140318')

# Define the visualization parameters.
vizParams = {
  'bands': ['B5', 'B4', 'B3'],
  'min': 0,
  'max': 0.5,
  'gamma': [0.95, 1.1, 1]
}

# Center the map and display the image.
Map.setCenter(-122.1899, 37.5010, 10); # San Francisco Bay
Map.addLayer(image, vizParams, 'False color composite')
Map

Map = geemap.Map()
Map
