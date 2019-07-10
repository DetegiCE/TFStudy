#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

data_file_name = 'simple_linear.txt'
xy=np.genfromtxt(open(data_file_name,'r'),dtype='float32')

print(np.shape(xy))

x_data = xy[:,0]
y_data = xy[:,2]

plt.plot(x_data, y_data, 'bo', alpha= 0.3)
plt.show()
