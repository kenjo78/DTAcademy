# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:12:18 2019

@author: Peter
"""

import tensorflow as tf
import keras
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images.ndim
train_images.shape

train_images.dtype
import matplotlib.pyplot as plt
digit = train_images[4]

plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

digit5 = train_images[5]
plt.imshow(digit5, cmap=plt.cm.binary)

train_images[0]

mnist