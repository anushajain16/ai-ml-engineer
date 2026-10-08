"""Calculate: Mean Squared Error"""

import numpy as np

y_true = np.array([3, 5, 7, 9])
y_pred = np.array([2, 5, 8, 10])

# Calculate Mean Squared Error
mse = np.mean((y_true - y_pred) ** 2)
print("Mean Squared Error:", mse)