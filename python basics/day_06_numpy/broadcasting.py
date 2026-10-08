"""Subtract the row means from a (1000, 50) matrix in one line, then do the same with column means. Explain the shapes involved."""

import numpy as np

arr = np.random.rand(1000, 50)
row_means = arr - arr.mean(axis=1, keepdims=True)
print(row_means)

col_means = arr - arr.mean(axis=0, keepdims=True)
print(col_means)