#-*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf

data_file_name = 'simple_linear.txt'
xy = np.genfromtxt(data_file_name, dtype='float32')

x_data = xy[:,0]
y_data = xy[:,2]

X = tf.placeholder('float32')
Y = tf.placeholder('float32')

#temporary value
temp_a = 0.5
temp_b = 0.5

a = tf.Variable(temp_a)
b = tf.Variable(temp_b)
y = a * X + b

#cost define and learning
cost = tf.reduce_mean(tf.square(y-Y)) #solve the mean of elements and return a value

#optimizer and learning define
opt = tf.train.GradientDescentOptimizer(0.001) #gradient descent
do_train = opt.minimize(cost)

#session initialize
init = tf.global_variables_initializer();

#train session
with tf.Session() as sess:
    sess.run(init)

    for i in range(0,5000):
        sess.run(do_train, feed_dict={X: x_data, Y: y_data})

        #logging
        if(i%100 == 0):
            cost_out = sess.run(cost, feed_dict = {X: x_data, Y: y_data})
            a_out = sess.run(a, feed_dict = {X: x_data, Y: y_data})
            b_out = sess.run(b, feed_dict = {X: x_data, Y: y_data})
            print(i, "session is performed. cost is ", cost_out, ", a is ", a_out,", b is ", b_out)
