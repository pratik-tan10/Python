#magic
%reload_ext autoreload
%autoreload 2
%matplotlib inline

#imports
from fastai.imports import *
from fastai.conv_learner import *
from fastai.model import *
from fastai.plots import *

import rasterio
from rasterio import plot
import matplotlib.pyplot as plt

#path setup
PATH = Path('/home/appy/project/EuroSat/Bands/')
train_path = PATH/'train'
classes = [str(f).split('/')[-1] for f in list(train_path.iterdir())]

#classes and size
files = []

for i in classes:
    paths =train_path/i
    files.append(list(paths.iterdir())[0])
classes_num = {}
for i in classes:
   
    folders = train_path/i
    classes_num[i] = len(list(folders.iterdir()))
    #print(f'{i} class has {len(list(folders.iterdir()))}')
plt.figure(figsize=(15,6))
plt.bar(classes_num.keys(), classes_num.values(), color='green')
plt.title('Land Use Classes & Size', fontsize=16)
plt.xlabel('Classes', fontsize=14)
plt.ylabel('Size', fontsize=14)
plt.tight_layout()
plt.savefig('classes.jpg')

