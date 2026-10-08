"""Given a query vector of shape (d,) and a matrix of shape (n, d), compute the distance from the query to every row with no loops.
You have: one point (a list of d numbers) and a table of n points.
Do: find how far the one point is from every point in the table. No loops.
Output: a list of n distances.
Hint: subtract, square, sum across columns, then take the square root.
"""

import numpy as np

def euclidean_distance(query, matrix):
    # Ensure the query is a 1D array and the matrix is a 2D array
    query = np.asarray(query)
    matrix = np.asarray(matrix)

    # Compute the squared differences
    squared_diff = (matrix - query) ** 2

    # Sum across columns (axis=1) to get the squared distances
    squared_distances = np.sum(squared_diff, axis=1)

    # Take the square root to get the Euclidean distances
    distances = np.sqrt(squared_distances)

    return distances

# Example usage
query = [1, 2, 3]
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                    [7, 8, 9]])

distances = euclidean_distance(query, matrix)
print("Distances from query to each row in the matrix:")
print(distances)