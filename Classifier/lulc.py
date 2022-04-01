from tensorflow.keras.models import Sequential 
from tensorflow.keras.backend import set_image_data_format 
from tensorflow.keras.layers import Conv2D, MaxPool2D, BatchNormalization 
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense 
from tensorflow.keras import optimizers, losses, utils 
from livelossplot import keras_plot 
set_image_data_format(‘channels_first’) 
model = Sequential()

