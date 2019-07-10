#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
import math

xy = []
n_count = 1999
x = 0.01
for i in range(n_count):
    y=math.pow(x-5, 2)+random.random()*5
    new_row = [x,y]
    xy.append(new_row)
    x=x+0.01

xy = np.array(xy)
x_data = xy[:,0]
y_data = xy[:,1]

plt.plot(x_data,y_data,'bo',alpha=0.3)
plt.show()
