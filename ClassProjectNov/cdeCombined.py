import numpy
import os
from osgeo import gdal
import numpy as np
from PIL import Image

os.chdir(r"C:\Users\Research Lab\Desktop\Pratik\ClassProj\CDL_2020_clip_20211020174535_329934016")
image = gdal.Open(r"merged.tif")

data1 = image.ReadAsArray()
print(data1.shape)
data = np.moveaxis(data1,0,-1)
'''k1 = data1[1,:,:]
k2 = data[:,:,1]
Image.fromarray(k1).show()
Image.fromarray(k2).show()
Image.fromarray(k2-k1).show()
print(data.ndim)'''


#Function to find probability of similarity
def prob(a,b,w1=0.7):
    if type(b)==type(True):
        return 0
    else:
        c = a==b
        N = len(a)
        p = (1-(sum(c))/N)*w1 + (1-len(set(b[c]))/N)*(1-w1)
        #p = len(set(b[c]))/N
        '''c w1 is weight to similarity
        w2 is weight to variety in crops
        '''
        return p

print(f"shape of data is {data.shape}")
m,n,o = data.shape
probM = numpy.zeros((m,n,8))

di = {0:np.array((-1,0)),1:np.array((-1,1)),2:np.array((0,1)),3:np.array((1,1)),4:np.array((1,0)),5:np.array((1,-1)),6:np.array((0,-1)),7:np.array((-1,-1))}
def Dij(i,j,dr):
    return (np.array((i,j))+di[dr])
for i in range(m):
    for j in range(n):
        #probM[i,j]=[]
        a = data[i,j,:]
        try:
            b0 = data[i-1,j,:]
        except:
            b0 = False
        try:
            b1 = data[i-1,j+1,:]
        except:
            b1 = False
        try:
            b2 = data[i,j+1,:]
        except:
            b2 = False
        try:
            b3 = data[i+1,j+1,:]
        except:
            b3 = False
        try:
            b4 = data[i+1,j,:]
        except:
            b4 = False
        try:
            b5 = data[i+1,j-1,:]
        except:
            b5 = False
        try:
            b6 = data[i,j-1,:]
        except:
            b6 = False
        try:
            b7 = data[i-1,j-1,:]
        except:
            b7 = False
        B = [b0,b1,b2,b3,b4,b5,b6,b7]
        p=[]
        for b in B:
            p.append(prob(a,b))
        probM[i,j]=p

print(f"shape of probability matrix: {probM   .shape}")
#print(probM)
#for i in range(8):
    
#    probImg.show()
#    probImg.save('probabilityImage_{}.tif'.format(i))
#
pcount = 0        
outRaster = numpy.zeros((m,n))

clusterN = 1
for i in range(m):
    for j in range(n):
        pb = probM[i,j]
        if pcount<20:
            print(pb)
            pcount+=1
        maxp = numpy.amax(pb)
        dr = numpy.where(pb==maxp)
        drt = dr[0]
        for each in range(len(drt)):
            dij = Dij(i,j,each)
            
            if maxp <0.01:
                outRaster[i,j] = clusterN
                clusterN+=1
            else:
                try:
                    testval = outRaster[tuple(dij)]
                    if testval != 0:
                        outRaster[i,j] = testval
                    elif testval==0:
                        outRaster[i,j] = clusterN
                        outRaster[tuple(dij)] = clusterN
                        clusterN+=1
                except:
                    pass

            
ResultImage = Image.fromarray(outRaster)
ResultImage.show()
ResultImage.save("ResultImage.tif")
