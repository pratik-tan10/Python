import os
from geopandas import GeoSeries, GeoDataFrame, read_file, gpd
from matplotlib import pyplot as plt
%matplotlib inline
input_file = 'nybb/nybb.shp'

boroDF = gpd.read_file(input_file)
boroDF

boroDF.index
boroDF.columns
boroDF.values

boroDF>values.shape
boroDF.values[0]
boroDF.columns
boroDF>values[1]
boroDF.values[1][1]
