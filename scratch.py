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
