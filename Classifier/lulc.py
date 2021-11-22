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

#images
fig = plt.figure(figsize=(12,10))
ax1 = plt.subplot(331);plt.axis('off');plot.show((rasterio.open(files[0])), ax=ax1, title=classes[0])
ax2 = plt.subplot(332);plt.axis('off');plot.show((rasterio.open(files[1])), ax=ax2, title=classes[1])
ax3 = plt.subplot(333);plt.axis('off');plot.show((rasterio.open(files[2])), ax=ax3, title=classes[2])

ax1 = plt.subplot(334);plt.axis('off');plot.show((rasterio.open(files[3])), ax=ax1, title=classes[3])
ax2 = plt.subplot(335);plt.axis('off');plot.show((rasterio.open(files[4])), ax=ax2, title=classes[4])
ax3 = plt.subplot(336);plt.axis('off');plot.show((rasterio.open(files[5])), ax=ax3, title=classes[5])

ax1 = plt.subplot(337);plt.axis('off');plot.show((rasterio.open(files[6])), ax=ax1, title=classes[6])
ax2 = plt.subplot(338);plt.axis('off');plot.show((rasterio.open(files[7])), ax=ax2, title=classes[7])
ax3 = plt.subplot(339);plt.axis('off');plot.show((rasterio.open(files[8])), ax=ax3, title=classes[8])

plt.tight_layout()

#Model
sz = 224
arch=resnet50
data = ImageClassifierData.from_paths(PATH, tfms=tfms_from_model(arch, sz))

learn = ConvLearner.pretrained(arch, data, precompute=True)
learn.fit(0.001, 2)

lrf=learn.lr_find(start_lr=1e-5, end_lr=1e-1)

learn.sched.plot_lr()
learn.sched.plot()
learn.fit(1e-5, 3, cycle_len=1)
learn.fit(1e-5, 3, cycle_len=1, cycle_mult=2)

learn.fit(1e-5, 3, cycle_len=1, cycle_mult=2)
lr = 1e-4
lrs = np.array([lr/12,lr/6,lr])
learn.fit(lrs, 2, cycle_len=1, cycle_mult=2) 
learn.unfreeze()
learn.fit(lrs, 3, cycle_len=1, cycle_mult=2) 
learn.fit(lrs, 2, cycle_len=1, cycle_mult=2) 

#Check results
log_preds,y = learn.TTA()
probs = np.mean(np.exp(log_preds),0)
log_preds = learn.predict()
preds = np.argmax(log_preds, axis=1)
preds
data.val_ds.fnames[0]

#Individual prediction
classes_dict = dict(enumerate(data.classes))
classes_dict
fn = data.val_ds.fnames[0]
pic1 = rasterio.open(str(PATH/fn))
plt.axis('off')
plot.show(pic1)
trn_tfms, val_tfms = tfms_from_model(arch, sz)
ds = FilesIndexArrayDataset([fn], np.array([0]), val_tfms, PATH)
dl = DataLoader(ds)
preds = learn.predict_dl(dl)
print(classes_dict[np.argmax(preds)] == 'AnnualCrop')
np.argmax(preds), classes_dict[np.argmax(preds)]
data.val_ds.fnames[2900]
fn = data.val_ds.fnames[2900]
pic2 = rasterio.open(str(PATH/fn))
plt.axis('off')
plot.show(pic2)

trn_tfms, val_tfms = tfms_from_model(arch, sz)
ds = FilesIndexArrayDataset([fn], np.array([2900]), val_tfms, PATH)
dl = DataLoader(ds)
preds = learn.predict_dl(dl)
print(classes_dict[np.argmax(preds)] == 'Pasture')
np.argmax(preds), classes_dict[np.argmax(preds)]
