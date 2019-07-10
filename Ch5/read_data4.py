#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

data_file_name='label_dots.txt'
xy=np.genfromtxt(data_file_name,dtype='float32')

x_data = xy[:,0]
y_data = xy[:,1]

xy = np.array(xy)
plt.plot(x_data,y_data,'bo',alpha=0.3)
plt.show()
