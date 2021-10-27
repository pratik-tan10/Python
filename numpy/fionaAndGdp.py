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

boroDF.describe()
#Transform Dataframe
boroDF.T
#sort dataframe
boroDF.sort_values(by = 'BoroCode', inplace = True, ascending = True)
boroDF.head()

boroDF[:2]
boroDF.sort_values(by = 'Shape_area', inplace = True, ascending = False)
boroDF[:2]

boroDF[['Shape_Araea', 'BoroName']]
boroDF[['Shape_Araea', 'BoroName']][:2]
boroDF[:2][['Shape_Araea', 'BoroName',  'Shape_Leng']]

