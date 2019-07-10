#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

xy = []
n_count = 300

#first group
temp_x = np.random.normal(3, 1, n_count)
temp_y = np.random.normal(3, 1, n_count)
for i in range(n_count):
    x = temp_x[i]
    y = temp_y[i]
    new_row = [x,y,1,0,0]
    xy.append(new_row)

#second group
temp_x = np.random.normal(6, 1, n_count)
temp_y = np.random.normal(6, 1, n_count)
for i in range(n_count):
    x = temp_x[i]
    y = temp_y[i]
    new_row = [x,y,0,1,0]
    xy.append(new_row)

#third group
temp_x = np.random.normal(1, 1, n_count)
temp_y = np.random.normal(7, 1, n_count)
for i in range(n_count):
    x = temp_x[i]
    y = temp_y[i]
    new_row = [x,y,0,0,1]
    xy.append(new_row)

xy = np.array(xy)
x_data = xy[:,0]
y_data = xy[:,1]
plt.plot(x_data, y_data, 'bo', alpha=0.3)
plt.show()
