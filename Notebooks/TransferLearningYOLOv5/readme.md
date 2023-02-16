---
jupyter:
  accelerator: GPU
  colab:
  gpuClass: standard
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.10.8
  nbformat: 4
  nbformat_minor: 1
---

::: {.cell .markdown id="mvofTeyVDAH3"}
```{=html}
<div style = "border-radius:10px; color: #3ABF5A; background-color: #3A3A3A">
    <h1 style  = "padding: 8px;">Swimming Pool Detection using YOLOv5</h1>
</div>
```
For some tasks, there are **pretrained models** that are already trained
on huge datasets using a vast computing resource. Trying to a build a
model from scratch for such tasks may be reinventing the wheel. We can
simply take the pretrained model and train it on our specific data for
some time and get very good accuracy withing a few hours, which would
have taken us weeks or even months if we had done all the model building
and training from scratch.

[YOLOv5](https://github.com/ultralytics/yolov5) is a really great
open-source objection detection model. Through **transfer-learning**,
this model can be easily trained to a custom dataset for detecting the
feature of our interest.

This tutorial will guide us on using this model for swimming pool
detection in satellite images.

First, we will see how to prepare the training data then we will train,
test and deploy the model.

-   [1 - Data Preparation](#1)
    -   [1.1 Getting satellite image](#1.1)
    -   [1.2 Clipping satellite Image](#1.2)
    -   [1.3 Annotating Images](#1.3)
-   [2 - Model Installation and Set up](#2)
-   [3 - Train the model](#3)
-   [4 - Testing the model](#4)
-   [5 - Deploying the model](#5)
:::

::: {.cell .markdown id="p6qsSPbQF8H0"}
`<a name = '1'>`{=html}`</a>`{=html}

## 1 - Data Preparation {#1---data-preparation}

For our swimming pool detection, we will need some satellite images. As
swimming pools are not easily identifiable in moderate-resolution images
such as Landsat, we will use high-resolution images from base maps. We
will use ArcMap, a desktop GIS software to save the satellite images.
This will require some manual work.
:::

::: {.cell .markdown}
`<a name = '1.1'>`{=html}`</a>`{=html}

## 1.1 Getting Satellite Images {#11-getting-satellite-images}

1.  Open ArcMap. From the drop-down of Add Data, select **Add Basemap**
    and choose the **Imagery**.
    `<img style = "width: 50%;" src = './Notebook jpgs/addBasemap.PNG'>`{=html}`<br>`{=html}

2.  Use the **Go to XY** tool. From the dropdown, change the unit to
    **Meters** .
    `<img style = "width: 50%;" src = './Notebook jpgs/gotoXY.PNG'>`{=html}`<br>`{=html}

For **longitude**, enter the value **-10962575**, and for **latitude**
enter value **3456760**. This will zoom to a portion of **San Antenio,
Texas**.

1.  From the main menu, go to **View** and to the **Layout View**.
    `<img src = './Notebook jpgs/GotoLayout.PNG'>`{=html}`<br>`{=html}

2.  Now, activate the **Layout** tools by right cleaning on the gray
    area above the display port, then checking the **Layout** tool.
    `<img src = './Notebook jpgs/activateLayoutTool.PNG'>`{=html}`<br>`{=html}

3.  From the **Layout** tool, click on **Change Layout**. Then choose
    **ISO A0 Landscape**, then click **finish** and wait for the changes
    to take effect.
    `<img src = './Notebook jpgs/changeLayout.PNG'>`{=html}`<br>`{=html}

4.  Now, click on the map area. It will show a bounding box (map frame),
    strech it\'s boundaries beyond the outline of the paper.
    `<figure>`{=html}
    `<img style = 'width: 45%; display: inline' src = './Notebook jpgs/before.PNG'>`{=html}
    `<figcaption>`{=html}Before stretching the map
    frame`</figcaption>`{=html} `</figure>`{=html} `<br>`{=html}
    `<figure>`{=html}
    `<img style = 'width: 45%; display: inline' src = './Notebook jpgs/after.PNG'>`{=html}`<br>`{=html}
    `<figcaption>`{=html}After stretching the map
    frame`</figcaption>`{=html} `</figure>`{=html}

You may want to change the scale at which the map is rendered. From the
**Standard Toolbar** change the scale to 1:2100 or higher.

`<img src = './Notebook jpgs/scale.PNG'>`{=html}`<br>`{=html}

Now it\'s time to save the map. We will export the map to jpeg format.
It definitely distorts the radiometric properties of the images, when
saving a satellite image for future analysis that might depend on
spectral signature it is not advisable. But for our purpose here, as we
can still identify swimming pools from resampled images, we are good to
go.

1.  From the main menu, go to **File** and click **Export Map** button.
    Save as type **JPEG** with the **resolution** of **150 dpi** and
    save at an appropriate location.
    `<img src = './Notebook jpgs/saveJPEG.PNG'>`{=html}`<br>`{=html}
:::

::: {.cell .markdown id="mEv1MxGxF8O3"}
`<a name = '1.2'>`{=html}`</a>`{=html}

## 1.2 Clipping Satellite Images {#12-clipping-satellite-images}

For object detection, we will need multiple smaller images. In each
image we will annotate the bounding box of every swimming pool we will
see for training. So, we need to clip the satellite image. For this we
will use [Python](https://www.python.org/downloads/). First make sure
you have python 3.x installed on your computer.

Go to the folder where you saved the image from step 1.1, then on the
address bar, type **cmd** then hit **enter** to open a **command
Prompt** at that directory. Alternatively, we can open the command
prompt first and change the directory to that location by running **cd
\'\<full path to the folder\>\'**
:::

::: {.cell .markdown id="YZcttoJcF8Tx"}
We will also need to install `Pillow` package for reading and writing
images and `numpy` for clipping images. When in that directory, run
following commands to install these packages. Be sure to remove the
dollar sign (\'\$\') if running directly in the command line.
:::

::: {.cell .code id="scrUwrTywgev"}
``` python
$ pip install numpy
```
:::

::: {.cell .code id="CBX3f9elwgO_"}
``` python
$ pip install Pillow
```
:::

::: {.cell .markdown id="vDanww0VF8XD"}
After the packages are installed, we will need to load required packages
for image clipping.

### Setting up
:::

::: {.cell .code id="MyMxFhWi7d68"}
``` python
import numpy as np
from PIL import Image
import os
```
:::

::: {.cell .markdown id="fcylrVuMI1uB"}
If we are running the code in command line, change the directory to the
folder containing the **LargeImage.jpg** .
:::

::: {.cell .code id="OIFclILhI2GR"}
``` python
os.chdir('/content/')
```
:::

::: {.cell .markdown id="HbwuImNb7fHN"}
### Read image
:::

::: {.cell .code id="SWyzAHGP7f9c"}
``` python
image = Image.open('LargeImage.jpg')
```
:::

::: {.cell .markdown id="nU50kwLP7gcc"}
### Convert image to numpy array
:::

::: {.cell .code id="k513EKZv7g58"}
``` python
im = np.asarray(image)
```
:::

::: {.cell .markdown id="Uiq5nYTH7hQ8"}
### Clipping Images

Output image will be of shape (M, N). This will split into x\*x images
of size (M,N) and a few corner images may also be produced of remainder
size. If we want the output be of certain size then provide then set M
and N to those values.
:::

::: {.cell .code id="v9RpprN78AFE"}
``` python
# Get shape and size of each output tile
x = 10
M = im.shape[0]//x
N = im.shape[1]//x

tiles = [im[x:x+M,y:y+N,:] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]
```
:::

::: {.cell .markdown id="dWDujOWH8V7j"}
### Save tiles as jpg
:::

::: {.cell .code execution_count="9" id="4omnSfTJxMPv"}
``` python
for idx, tile in enumerate(tiles):
  tileImage = Image.fromarray(tile)
  tileImage.save(f'tile_{idx}.jpg')
```
:::

::: {.cell .markdown id="JHYo5I6O8daz"}
### Download images from colab to local disk

This part only applies if we use colab to split the image into tiles
which we will upload to roboflow for annotation. Otherwise, our tiles
are already saved on our local disk and we are ready to move to image
annotation part.
:::

::: {.cell .code id="p8T10k3301V1"}
``` python
from google.colab import files
files.download('/content')
```
:::

::: {.cell .markdown id="N_7IDe03F8Z6"}
`<a name = '1.3'>`{=html}`</a>`{=html}

## 1.3 Annotating Images {#13-annotating-images}

We will use [roboflow](https://roboflow.com/), which is a great tool for
annotating images or videos, to annotate the images with bounding box.
First we have to sign up at [roboflow](https://roboflow.com/), which can
be done with any email or github account. We can create a new workspace
as a hobbies type and give any name.

We can skip inviting other people and create a public workspace. Create
on **new project** and **Explore Solo** and we are detecting **Swimming
pools**. For license type, we can choose any of the options.

Now, we can either drag-and-drop images or add files or folder. After it
finishes uploading images, click on **save and continue** on the
top-right corner.
`<img src = './Notebook jpgs/dragAndDropImages.PNG'>`{=html}`<br>`{=html}

Next step is to assign different images to different person. But as
there is only one person in this workspace, simply assign images to that
account.

Now, for the actual annotation, click on the first image and start
drawing a rectanglular bounding box around the image. After drawing one
polygon hit enter to save it. We can draw multiple polygons if there are
multiple swimming pools or not draw any if there is no swimming pool in
the image.
`<img src = './Notebook jpgs/drawBoundaries.PNG'>`{=html}`<br>`{=html}

After finishing the **Annotation**, go to back. It will show how many
images are labelled or unlabelled and ask to **add the labelled images
to dataset**. Click there. Keep 70% for training and 15% each for
validation and testing. Click on **Add Images**.

Now click on **Generate New Version** . Keep everything default. Go to
number 5 **Generate**.
`<img src = './Notebook jpgs/Generate.PNG'>`{=html}`<br>`{=html}

It will generate a version of data. Go to **Export**, and in the
**format**, choose **YOLOv5 PyTorch** annd click on **Continue**. This
will generate a **download code** that can be run in jupyter notebook or
colab. Copy this code, we will need this to download our dataset, and
also pay attention to the warning.
`<img src = './Notebook jpgs/ChangeModelVersion.PNG'>`{=html}`<br>`{=html}
:::

::: {.cell .markdown id="0_Vn8bexZGnl"}
`<a name = '2'>`{=html}`</a>`{=html}

## 2 - Model Installation and setup {#2---model-installation-and-setup}
:::

::: {.cell .markdown id="7pBrjSmyF8fi"}
`<a name = '2.1'>`{=html}`</a>`{=html}

## 2.1 Installing yolov5 {#21-installing-yolov5}

We can clone the **yolov5** github repository to obtain the pretrained
model. We will need to install some dependencies for running this model.
Also, we will install **roboflow**, which we will need to obtain the
data using the **download code** copied at the end of the previous step.
:::

::: {.cell .code id="kTvDNSILZoN9"}
``` python
#clone YOLOv5 and 
!git clone https://github.com/ultralytics/yolov5  # clone repo
%cd yolov5
%pip install -qr requirements.txt # install dependencies
%pip install -q roboflow

import torch
import os
from IPython.display import Image, clear_output  # to display images

print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")
```
:::

::: {.cell .markdown id="EkLq6fwlF8ct"}
`<a name = '2.2'>`{=html}`</a>`{=html}

## 2.2 Load Data from roboflow {#22-load-data-from-roboflow}

In the cell below, paste the **download code** copied from roboflow to
obtain the data we prepared in step [1.3](#1.3)
:::

::: {.cell .code id="WZphSQ6WT6EW"}
``` python
from roboflow import Roboflow
rf = Roboflow(api_key="<personal_key>") # Replace
project = rf.workspace("<workspace_name>").project("<project_name>") # Replace
dataset = project.version(2).download("yolov8")
```
:::

::: {.cell .code id="2jjT5uIHo6l5"}
``` python
# set up environment
os.environ["DATASET_DIRECTORY"] = "/content/datasets"
```
:::

::: {.cell .markdown id="BomwNGHdZ7vV"}
`<a name = '3'>`{=html}`</a>`{=html}

## 3 - Train the model {#3---train-the-model}

(**Already have the best.pt ? click [here](#5) to go to the detection
section**.) Run the following cell to train the model.
:::

::: {.cell .code id="eaFNnxLJbq4J"}
``` python
!python train.py --img 640 --batch 16 --epochs 50 --data {dataset.location}/data.yaml --weights yolov5s.pt --cache
```
:::

::: {.cell .markdown id="jtmS7_TXFsT3"}
`<a name = '3'>`{=html}`</a>`{=html}

## 3 - Detect swimming pools on test image {#3---detect-swimming-pools-on-test-image}

In the following cell make sure the location of **best.pt** is correct
and the path of folder containing test images is also correct. This
exact same code will also be used for detecting in the future, but we
will need to change the location of **best.pt** and folder containing
images.

The parameter `conf` is set to 0.2. Setting it low will detect more
swimming pools but will also detect other things as swimming pool
meaning it will increase the **comission error**, and setting it high
will detect fewer swimiming pool meaning it will increase the **omission
error**. We can play around with this value to see what works best.
:::

::: {.cell .code id="G_SwLam8b1jr"}
``` python
!python detect.py --weights /content/yolov5/runs/train/exp/weights/best.pt --img 640 --conf 0.2 --source /content/datasets/SwimmingPoolDataset-1/test/images
```
:::

::: {.cell .markdown id="bhzuIzCtdpCE"}
Now, let\'s visually inspect how well the model did.
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":877}" id="GXxGLprYd4g_" outputId="cb00eb38-1763-4f36-c456-79df03915a12"}
``` python
from matplotlib import pyplot as plt
from numpy import array
from PIL import Image

for imageName in glob.glob('/content/yolov5/runs/detect/exp2/*.jpg'): #assuming JPG
    image = Image.open(imageName)
    plt.imshow(array(image))
    plt.show()
    print("\n")
```
:::

::: {.cell .markdown id="9L7nS_cPe8Ti"}
It seems the model is doing preety good job. As the storage of this
colab session is temporary, if we want to use this model in the future
without training it again, we will need to save the model weights. Run
the following code to download the best weights.
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":17}" id="7iiObB2WCMh6" outputId="6926c120-51b5-4068-e6f2-951088c97142"}
``` python
#export your model's weights for future use
from google.colab import files
files.download('./runs/train/exp/weights/best.pt')
```

::: {.output .display_data}
    <IPython.core.display.Javascript object>
:::

::: {.output .display_data}
    <IPython.core.display.Javascript object>
:::
:::

::: {.cell .markdown id="deLjX2Jkffji"}
`<a name = '5'>`{=html}`</a>`{=html}

## 5 - Deploying the model {#5---deploying-the-model}

Now we have the weights saved, we have no need to train the model if we
want to simply use the model for detecting swimming pools. For this we
will need to prepare the image on which we want to detect the swimming
pool by following the method described in [section 1](#1).

If we want to use colab for detection, we will have to upload the images
and weights to the collab session storage. Then, for the following
cells, the location of best.pt,location of image on which we want to run
the detection need to be changed. By running the cell below with
appropriate parameters we can detect the images
:::

::: {.cell .code execution_count="12" id="TWjjiBcic3Vz"}
``` python
!python detect.py --weights /content/best.pt --img 640 --conf 0.2 --source /content/sample_data/exp
```
:::

::: {.cell .markdown id="CRlosxB_g61S"}
Now run the following cell after changing the location of output images,
to visually inspect them.
:::

::: {.cell .code execution_count="17" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":877}" id="W-wgpDwfqIbI" outputId="fa619ded-86e2-46d2-c38b-ab159f7a9590"}
``` python
from matplotlib import pyplot as plt
from numpy import array
from PIL import Image

for imageName in glob.glob('/content/yolov5/runs/detect/exp2/*.jpg'): #assuming JPG
    image = Image.open(imageName)
    plt.imshow(array(image))
    plt.show()
    print("\n")
```

::: {.output .display_data}
![](imgs/one.png)
:::

::: {.output .stream .stdout}
:::

::: {.output .display_data}
![](imgs/two.png)
:::

::: {.output .stream .stdout}
:::

::: {.output .display_data}
![](imgs/three.png)
:::

::: {.output .stream .stdout}
:::
:::

::: {.cell .markdown id="9cqzJfcpieZZ"}
**Congratulations**!! Now you know:

-   how to create training data for objection,
-   how to use a transfer learning and
-   how to deploy a trained model.

Good luck on your learning journey.
:::
