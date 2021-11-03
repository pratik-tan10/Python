#Library Imports
%matplotlib inline

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pysal as ps
import geopandas as gpd
from sklearn import cluster
from sklearn.preprocessing import scale

sns.set(style="whitegrid")

# Adjust this to point to the right file in your computer
abb_link = '../data/listings.csv.gz'
zc_link = '../data/Zipcodes.geojson'

lst = pd.read_csv(abb_link)
varis = ['bedrooms', 'bathrooms', 'beds']
aves = lst.groupby('zipcode')[varis].mean()
aves.info()

