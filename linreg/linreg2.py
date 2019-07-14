#-*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf

data_file_name = 'simple_linear.txt'
xy = np.genfromtxt(data_file_name, dtype='float32')

x_data = xy[:,0]
y_data = xy[:,2]

X = tf.placeholder('float32')
Y = tf.placeholder('float32')

temp_a = 0.5
temp_b = 0.5

a = tf.Variable(temp_a)
b = tf.Variable(temp_b)
y = a * X + b

cost = tf.reduce_mean(tf.square(y-Y))

opt = tf.train.GradientDescentOptimizer(0.001);
do_train = opt.minimize(cost)

init = tf.global_variables_initializer()

#set graphic parameter
a_out = 0.1
b_out = 0.1

with tf.Session() as sess:
    sess.run(init)

    for i in range(0,5000):
        sess.run(do_train, feed_dict = {X: x_data, Y: y_data})
        if(i%100 == 0):
            cost_out = sess.run(cost, feed_dict = {X: x_data, Y: y_data})
            a_out = sess.run(a, feed_dict = {X: x_data, Y: y_data})
            b_out = sess.run(b, feed_dict = {X: x_data, Y: y_data})

import matplotlib.pyplot as plt

plt.plot(x_data, y_data, 'ro', alpha=0.01)

x_sample = np.linspace(np.amin(x_data), np.amax(x_data), 20)
y_sample = a_out * x_sample + b_out

plt.plot(x_sample, y_sample, '*', label="x_sample")
plt.legend()
plt.show()
