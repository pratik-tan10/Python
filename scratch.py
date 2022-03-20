import numpy as np
import cv2
from matplotlib import pyplot as plt]
from copy import deepcopy

img = cv2.imread("im0.png",0)
img

def wind(imgage)
    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    cv2.imshow("window",image)
    cv2.watiKey(10000)
    cv2.destroyAllWindows()
wind(img)
imgCol = cv2.imread("im0.png",1)
wind(imgCol)

imgCol1 = deepcopy(imgCol)
cv2.circle(imgCol, (127,1200),100,(125,130,14),20)
wind(circle)

imgN1 = cv2.imread("double.png",1)
wind(imgN)

imgN = deepcopy(imgN1)
def click2circle(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBCLIK:
        cv2.circle(imgN,(x,y),50,(225,0,0),4)
    
cv2.namedWindow("differences", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("differences")

while True:
    cv2.imshow("differences",imgN)
    a = cv2.waitKey(1)
    if a==27:
        break
cv2.destroyAllWindows()

b,g,r = cv2.split(imgCol)
imgCol
imgCol2 = cv2.merge((b,g,r))
wind(imgCol2)

imgres = cv2.resize(imgCol, dsize = None,fx=0.2,fy=0.2,interpolation = cv2.INTER_CUBIC)
cv2.imshow("window",imgres)
cv2.waitKey(10000)
cv2.destroyAllWindows()

cropped = imgres[210:368,300,570]
wind(cropped)
cv2.imwrite("cropped.png",cropped)

crops = cv2.imread("crops.png",0)
wind(crops)
sobelx = cv2.Sobel(crops,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(crops,cv2.CV_8U,0,1,ksize=3)
wind(sobelx)
wind(sobely)

laplacian = cv2.Laplacian(crops, cv2.CV_8U)
wind(laplacian)

edges = cv2.Canny(crops,100,200)
wind(edges)

bbal = cv2.imread("basketball.jpg",1)
wind(bbal)
edges = cv2.Canny(bbal,150,400)
wind(edges)

lines = cv2.HoughLines(edges, 1,np.pi/180,200)
lines

for iterator in lines:
    rho = iterator[0][0]
    theta = iterator[0][1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*(a))
    x2 = int(x0-1000*(-b))
    y1 = int(y0-1000*(a))
    cv2.line(bbal,(x1,y1),(x2,y2),(0,0,255),2)

wind(bbal)

#---------------------------------------------------------
imgN1 = cv2.imread("double.png",1)
diffs = np.array([[538,109],[1203,739],[758,137],[1240,467]])
def eucliD(x1,y1,x2,y2):
    return int(np.sqrt((x1-x2)**2+(y1-y2)**2))

imgN = deepcopy(imgN1)
def click2circle(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBCLIK:
        for diff in diffs:
            if euclidD(x,diff[0],y,diff[1])<15:
                cv2.circle(imgN,(x,y),50,(225,0,0),4)
    
cv2.namedWindow("differences", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("differences")

while True:
    cv2.imshow("differences",imgN)
    a = cv2.waitKey(1)
    if a==27:
        break
cv2.destroyAllWindows()

hsv = cv2.cvtColor(imgN1, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(imgN1, cv2.COLOR_BGR2GRAY)
wind(hsv)
wind(gray)
r,t = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
wind(t)

lena = cv2.imread("lena.jpg",0)
wind(lena)
hist = calcHist([lena],[0],None,[256],[0,256])
hist
xaxis = np.arange(256).reshape(256,1)
hist = np.hstack([xaxis,hist]).astype(int)
plt.hist(lena.flatten(),256,[0,256])
plt.show
equ = cv2.eualizeHist(lena)
res = np.hstack(lena,equ)
wind(res)

blur = cv2.blur(lena,(7,7))
wind(blur)
blurG = cv2.GaussianBlur(lena,(5,5),0)
res = np.hstack(lena,blurG)
wind(res)

img = cv2.imread("mbike.jpg",1)
imgCL = np.float32(img.reshape((-1,3)))
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,15,1.0)
k = 4
ret,lab,center = cv2.kmeans(imgCL,K,None,10,cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[lab.flatten()]
res2 = res.reshape((img.shape))
wind(res2)

pathB = "c:/Users/Alome/Documents/Before/"
pathA = "c:/Users/Alome/Documents/After/"
BEF = []
AFT = []
for i in range(1,8):
    BEF.append(cv2.imread(pathB+"B"+str(i)+".tif",0)[4200:4700,2900:3500])
    BEF.append(cv2.imread(pathA+"B"+str(i)+".tif",0)[4200:4700,2900:3500])
    
BEF32 = []
AFT32 = []
for i in range(7):
    BEF332.append(np.float32(cv2.equalizeHist(BEF[i])))
    AFT332.append(np.float32(cv2.equalizeHist(AFT[i])))
wind(cv2.equalizeHist(BEF[0]))

before = cv2.merge((BEF32[0],BEF32[1],BEF32[1],BEF32[3],BEF32[4],BEF32[5],BEF32[6]))
beforeReady = before.reshape((-1,7))
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,1)
ret,label,center = cv2.kmeans(beforeReady,6,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((before.shape))
beforeF = deepcopy(res2[:][:,:,:3])
wind(beforeF)


after = cv2.merge((AFT32[0],AFT32[1],AFT32[1],AFT32[3],AFT32[4],AFT32[5],AFT32[6]))
afterReady = after.reshape((-1,7))
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,1)
ret,label,center = cv2.kmeans(afterReady,6,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((after.shape))
afterF = deepcopy(res2[:][:,:,:3])
wind(afterF)

beforeafter = np.hstack(beforeF,afterH)

d = 0; q=0
for i in range(len(afterF)):
    for j in range(len(afterF[i])):
        if np.sum(afterF[i][j])==510:
            d+=1
            if (np.sum(beforeF[i][j])==369 or np.sum(beforeF[i][j])==251):
                q+=1
print("Total burned area:",d*900,"square meters.")
print("Forest burned area:",q*900,"square meters.")
