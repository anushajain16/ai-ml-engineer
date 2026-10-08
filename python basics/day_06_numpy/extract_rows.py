"""Return only rows whose row sum is greater than 100."""

import numpy as np

X = np.array([
    [10, 20, 30],
    [5,  15, 25],
    [100, 200, 300],
    [7,  8,  9]
])

arr_sum = np.sum(X, axis=1)
filtered_rows = X[arr_sum > 100]
print("Rows with sum greater than 100:")
print(filtered_rows)

