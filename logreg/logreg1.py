#-*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

train_x_data_all = mnist.train.images
train_y_data_all = mnist.train.labels

print("train_x_data shape is ", np.shape(train_x_data_all), ", train_y_data shape is ", np.shape(train_y_data_all))

temp_x = np.reshape(train_x_data_all, (55000,28,28))
view_1st_digit = temp_x[0]
