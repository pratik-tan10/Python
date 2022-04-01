from tensorflow.keras.models import Sequential 
from tensorflow.keras.backend import set_image_data_format 
from tensorflow.keras.layers import Conv2D, MaxPool2D, BatchNormalization 
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense 
from tensorflow.keras import optimizers, losses, utils 
from livelossplot import keras_plot 
set_image_data_format(‘channels_first’) 
model = Sequential()

model.add(Conv2D(28, (3, 3), padding=’same’,input_shape=(13, 64, 64))) 
model.add(Activation(‘relu’)) 
model.add(Conv2D(28, (3, 3), padding=’same’)) 
model.add(Activation(‘relu’)) 
model.add(MaxPool2D(2,2)) 
model.add(Conv2D(56, (3, 3),padding=’same’)) 
model.add(Activation(‘relu’)) 
model.add(Conv2D(56, (3, 3), padding=’same’)) 
model.add(Activation(‘relu’)) 
model.add(MaxPool2D(2,2)) 
model.add(Conv2D(112, (3, 3), padding=’same’)) 
model.add(Activation(‘relu’)) 
model.add(Conv2D(112, (3, 3), padding=’same’)) 
model.add(Activation(‘relu’)) 
model.add(MaxPool2D(2,2)) 
model.add(Flatten()) 
model.add(Dense(784)) 
model.add(Activation(‘relu’)) 
model.add(Dropout(0.6)) 
model.add(Dense(10)) 
model.add(Activation(‘sigmoid’)) 
adam = optimizers.Adam(lr=0.001) 
model.compile(optimizer=adam, loss=losses.binary_crossentropy, metrics=[‘accuracy’])
