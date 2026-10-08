"""Compute cosine similarity between a query vector and every row of a matrix, then return the indices of the top-5 most similar rows"""

import numpy as np

def cosine_similarity(query, matrix):
    # Ensure the query is a 1D array and the matrix is a 2D array
    query = np.asarray(query)
    matrix = np.asarray(matrix)

    # Normalize the query vector
    query_norm = query / np.linalg.norm(query)

    # Normalize the matrix rows
    matrix_norm = matrix / np.linalg.norm(matrix, axis=1, keepdims=True)

    # Compute cosine similarity
    similarity = np.dot(matrix_norm, query_norm)

    return similarity

# Example usage
query = [1, 2, 3]
matrix = np.array([[1, 2, 3],
                     [4, 5, 6],
                    [7, 8, 9],
                     [1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])
result = cosine_similarity(query, matrix)
# Get the indices of the top-5 most similar rows
top_5_indices = np.argsort(result)[::-1][:5]
print("Cosine similarity scores:")
print(result)
print("Indices of the top-5 most similar rows:")
print(top_5_indices)