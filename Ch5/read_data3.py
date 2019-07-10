#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

data_file_name = 'x_square.txt'
xy=np.genfromtxt(data_file_name,dtype='float32')

x_data = xy[:,0]
y_data = xy[:,1]

plt.plot(x_data,y_data,'bo',alpha=0.3)
plt.show()
