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
