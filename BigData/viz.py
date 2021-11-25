!conda/pip install pyshp
import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
#initialize visualization set
sns.set(style=”whitegrid”, palette=”pastel”, color_codes=True) sns.mpl.rc(“figure”, figsize=(10,6))

#open vecotr map
#opening the vector map
shp_path = “\\District_Boundary.shp”
#reading the shape file by using reader function of the shape lib
sf = shp.Reader(shp_path)

print(len(sf.shapes()))

print(sf.records())

print(sf.records()[1][0])

Output= Barmer
