"""Given a 1D array, replace all negative values with 0 and all values above 100 with 100, without loops"""

import numpy as np

arr = np.array([-10,20,30,40,45,75,-23,-45,-65,101,103,130,150,200])

arr[arr<0] = 0
arr[arr>100] = 100
print(arr)