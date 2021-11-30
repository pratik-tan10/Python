fc = r'AgriParclesWIth_Categories'
import numpy as np

ds = arcpy.Describe(fc)
fname = 'CategoryVector'
fields = ['SHAPE@',fname,'OBJECTID_1']

i = 0
vectorList = []
with arcpy.da.SearchCursor(fc, fields) as rows:
    for row in rows:
        if i ==2: break
        arcpy.MakeFeatureLayer_management(fc,'selector')

i = 0
vectorList = []
with arcpy.da.SearchCursor(fc, fields) as rows:
    for row in rows:
        i = i+1
        if 'one' in row[1]:
            continue
        else:
            strList = (row[1].replace(' ','').split(','))
            vector =(row[2], [int(x) for x in strList])
            vectorList.append(vector)
            #i = i+1
            j = row[2]

def prob(a,b,w1=0.7):
    try:
        c = a==b
        N = len(a)
        p = ((sum(c))/N)*w1 + (1-len(set(b[c]))/N)*(1-w1)
        #print(f"a:{a},b:{b},c:{c},p:{p}")
        #p = len(set(b[c]))/N
        '''c w1 is weight to similarity
        w2 is weight to variety in crops
        '''
        return p
    except: return 0

ProbM = np.zeros((i,i))
ProbM.shape

for each in vectorList:
    ii = each[0]-1
    a = np.array(each[1])
    for col in vectorList:
        jj = col[0]-1
        b = np.array(col[1])
        ProbM[ii,jj]=prob(a,b)

P1 = ProbM[0]
M1 = np.mean(P1)
MX1 = np.max(P1)
MD1 = np.median(P1)
C1 = M1+ 0.5*(MX1-MD1)
W1 = np.where(P1>C1)
print(W1)
i1 = len(W1[0])
print(P1[W1])
checkM1 = 
for each in W1:
    pass

#arcpy.MakeFeatureLayer_management("C:/data/mexico.gdb/cities","cities_lyr",)
a = 'hey'
fname = 'name'
print(f"{fname}='{a}'")

def y(a,b):
    op= ProbM[a-1,b-1]
    if op>=0.7:
        print( f"merge {op}")
    else: print(f"Dont {op}")

y(334,319)
