#This code is useful to convert neighbour table into neighbour matrix
#Read Neighbour csv table
import pandas as pd
df = pd.read_csv(r"C:\Users\Research Lab\Desktop\Pratik\ClassProj\neighbour.csv")

#Get maximum row and colums in csv
r = max(df['src_OBJECTID_1'])

#Initialize a zero square matrix with size of no of polygons
import numpy as np
R = np.eye(r)

#Get colums names
df.columns

#Subset only required source and neighbour colums from database
#This will be used to change neighbourhood information in matirx
Ni = df[['src_OBJECTID_1', 'nbr_OBJECTID_1']]

#Iterate through each row and create a tuple of each neighbour location in matrix
l=[]
i=0
for row in Ni.iterrows():
    x = ((row[1][0]), row[1][1])
    l.append(x)
    i=i+1

#For each location tuple, update from zero to 1
for each in l:
    R[each[0],each[1]]=1
