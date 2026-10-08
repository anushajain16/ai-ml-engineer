"""Implement a linear regression prediction"""

import numpy as np

X = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

weights = np.array([0.5, 2])
bias = 1

# Compute the linear regression prediction
predictions = np.dot(X, weights) + bias
print("Predictions:")
print(predictions)