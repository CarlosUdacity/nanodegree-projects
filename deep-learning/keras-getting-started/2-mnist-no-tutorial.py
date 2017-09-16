from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.losses import categorical_crossentropy
from keras.optimizers import Adadelta, Adam, SGD
from keras import backend as K


# Initial variables
batch_size = 128
num_classes = 10
epochs = 12
img_rows, img_cols = 28, 28

# Loads the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Depending on backend (Tensorflow or Theano), organizes tensors in different shape
if K.image_data_format() == 'channels_last':
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
else:
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)

# Input preprocessing: normalizing data
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# Also transforming targets from a scalar in a 10-shaped vector
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# Model topology
model = Sequential()
model.add(Conv2D(4, kernel_size=(1, 1), strides=(1, 1), activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(8, kernel_size=(2, 2), strides=(2, 2), activation='relu'))
model.add(Conv2D(12, kernel_size=(2, 2), strides=(2, 2), activation='relu'))
model.add(Flatten())
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(10, activation='softmax'))

# Compile and train
model.compile(loss=categorical_crossentropy, optimizer=SGD(), metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test))

# Print final scores
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss: \t', score[0])
print('Test accuracy: \t', score[1])
