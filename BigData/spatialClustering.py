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

#additional Variables
types = pd.get_dummies(lst['property_type'])
prop_types = types.join(lst['zipcode'])\
                  .groupby('zipcode')\
                  .sum()
prop_types_pct = (prop_types * 100.).div(prop_types.sum(axis=1), axis=0)
prop_types_pct.info()
aves_props = aves.join(prop_types_pct)

#Standarize columns
db = pd.DataFrame(\
                 scale(aves_props), \
                 index=aves_props.index, \
                 columns=aves_props.columns)\
       .rename(lambda x: str(int(x)))

#Plot
zc = gpd.read_file(zc_link)
zc.plot(color = 'red');

#Combine two data sets
zdb = zc[['geometry', 'zipcode', 'name']].join(db, on='zipcode').dropna()

f, ax = plt.subplots(1, figsize=(9, 9))

zc.plot(color='grey', linewidth=0, ax=ax)
zdb.plot(color='red', linewidth=0.1, ax=ax)

ax.set_axis_off()

plt.show()

#GeoDemographic Analysis
cluster.KMeans?

km5 = cluster.KMeans(n_clusters=5)
