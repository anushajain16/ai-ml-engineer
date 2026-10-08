"""Find the index of the maximum value. Then modify the problem to find all indices containing the maximum value."""

import numpy as np

arr = np.array([10,5,30,20,30])
# Find the index of the maximum value
max_index = np.argmax(arr)
print("Index of the maximum value:", max_index)

# Find all indices containing the maximum value
max_value = np.max(arr)
all_max_indices = np.where(arr == max_value)[0]
print("All indices containing the maximum value:", all_max_indices)