import pywt
import cv2
import numpy as np

# This function does the coefficient fusing according to the fusion method
def fuseCoeff(cooef1, cooef2, method):

    if (method == 'mean'):
        cooef = (cooef1 + cooef2) / 2
    elif (method == 'min'):
        cooef = np.minimum(cooef1,cooef2)
    elif (method == 'max'):
        cooef = np.maximum(cooef1,cooef2)
    else:
        cooef = []

    return cooef
# Params
FUSION_METHOD = 'mean' # Can be 'min' || 'max || anything you choose according theory

# Read the two image
I1 = cv2.imread('i1.bmp',0)
I2 = cv2.imread('i2.jpg',0)
# We need to have both images the same size
I2 = cv2.resize(I2,I1.shape) # I do this just because i used two random images
## Fusion algo

# First: Do wavelet transform on each image
wavelet = 'db1'
cooef1 = pywt.wavedec2(I1[:,:], wavelet)
cooef2 = pywt.wavedec2(I2[:,:], wavelet)
# Second: for each level in both image do the fusion according to the desire option
fusedCooef = []
for i in range(len(cooef1)-1):

    # The first values in each decomposition is the apprximation values of the top level
    if(i == 0):

        fusedCooef.append(fuseCoeff(cooef1[0],cooef2[0],FUSION_METHOD))

    else:

        # For the rest of the levels we have tupels with 3 coeeficents
        c1 = fuseCoeff(cooef1[i][0],cooef2[i][0],FUSION_METHOD)
        c2 = fuseCoeff(cooef1[i][1], cooef2[i][1], FUSION_METHOD)
        c3 = fuseCoeff(cooef1[i][2], cooef2[i][2], FUSION_METHOD)

        fusedCooef.append((c1,c2,c3))
# Third: After we fused the cooefficent we nned to transfor back to get the image
fusedImage = pywt.waverec2(fusedCooef, wavelet)

# Forth: normmalize values to be in uint8
fusedImage = np.multiply(np.divide(fusedImage - np.min(fusedImage),(np.max(fusedImage) - np.min(fusedImage))),255)
fusedImage = fusedImage.astype(np.uint8)
