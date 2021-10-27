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

bpop = [200000,22000,60000,111000,256000]
boroDF['Population'] = bpop
boroDF.tail()
from pandas import Series
population = Series({'Manhattan': 154882,
                     'Bronx' : 258254,
                     'Brooklyn' : 598324,
                     'Queens' : 256789,
                     'Staten Island' : 468730})
boroDF = boroDF.set_index('BoroName')
boroDF['Population'] = population


