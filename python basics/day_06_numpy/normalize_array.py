"""Given a 1D NumPy array, normalize it so that its values lie between 0 and 1."""

import numpy as np

arr = np.array([10,20,30,40,50])

arr_min = np.min(arr)
arr_max = np.max(arr)

normalized_arr = (arr - arr_min)/(arr_max-arr_min)
print("Normalized array:")
print(normalized_arr)