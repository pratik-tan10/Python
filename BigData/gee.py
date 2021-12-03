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
