#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

xy = []
n_count = 1999
a = 3
b = 4
mean, std = 20, 3 #mean and standard deviation
temp_x = np.random.normal(mean, std, n_count)
temp_b = np.random.normal(0, 3, n_count)
#np.random.normal(mean, st.dev, n)

for i, x in enumerate(temp_x):
    y = a*x + b + temp_b[i]
    new_row = [x,y]
    xy.append(new_row)

xy = np.array(xy)
x_data = xy[:,0]
y_data = xy[:,1]
plt.plot(x_data,y_data,'bo',alpha=0.3)
plt.show()
