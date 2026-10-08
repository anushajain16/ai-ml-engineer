"""Standardize each column of a 2D array to mean 0 and standard deviation 1. Then do min-max scaling to [0, 1]."""

import numpy as np

X = np.array([[1,22,3,4,5],[100,200,300,400,500]])

mean = X.mean(axis=0)
std = X.std(axis=0)
standardized_X = (X - mean) / std
print("Standardized array:")
print(standardized_X)

# Min-Max Scaling
min_val = X.min(axis=0)
max_val = X.max(axis=0)
min_max_scaled_X = (X - min_val) / (max_val - min_val)
print("Min-Max Scaled array:")
print(min_max_scaled_X)