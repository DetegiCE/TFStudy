#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

xy = []
n_count = 1999
x = 0.01
a = 3
b = 4

for i in range(n_count):
    new_row = [x, a*x, a*x+b]
    xy.append(new_row)
    x = x + 0.01

xy = np.array(xy)
x_data = xy[:,0]
y_data = xy[:,2]
plt.plot(x_data,y_data,'bo',alpha=0.3)
plt.show()
