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
