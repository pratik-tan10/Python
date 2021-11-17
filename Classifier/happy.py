#Imports
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import tensarflow as tf
import numpy as np
import cv2
import os

#Reading Images
plt.imshow(img)

cv2.imread("basedata/train/happy/1.PNG").shape

train = ImageDataGenerator(rescale = 1/255)
validation = ImageDataGenerator(rescale = 1/255)
train_dataset = train.flow_from_directory('basedata/train/',rarget_size = (200,200), batch_size = 3,\
class_mode = 'binary')

#Loading validation dataset
validation_dataset = train.flow_from_directory('basedata/validation/',rarget_size = (200,200), batch_size = 3,\
class_mode = 'binary')

#Looking at indices of classes
train_dataset.class_indices

#Looking at class labels of training datasets
train_dataset.classes
