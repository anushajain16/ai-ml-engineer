"""Make a 5x5 matrix with values 1 to 25, then extract the border and the inner 3x3."""

import numpy as np

matrix = np.arange(1,26).reshape(5, 5)
print(matrix)

# Extract the border
border = matrix.copy()
border[1:4, 1:4] = 0
print("Border of the matrix:")  
print(border)

# Extract the inner 3x3
inner_matrix = matrix[1:4,1:4]
print("Inner 3x3 matrix:")
print(inner_matrix)
