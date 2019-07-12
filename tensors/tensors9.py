import numpy as np

a = np.arange(6)
print("first \n",a)

a = np.reshape(a, [2,3])
print("second \n",a)

a = np.reshape(a, [3,2])
print("thrid \n",a)
