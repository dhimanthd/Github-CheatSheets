import numpy as np

# Load the transformation matrix from the .npy file
transform_matrix = np.load('central_to_car_transform.npy')

# Print the shape and data type of the matrix
print("Matrix shape:", transform_matrix.shape)
print("Data type:", transform_matrix.dtype)

# Access and analyze the individual elements of the matrix
# Example: Print the value at row 0, column 0
print("Element at (0, 0):", transform_matrix[0, 0])

# Perform further analysis or computations with the matrix as needed
# Example: Compute the inverse of the matrix
inverse_matrix = np.linalg.inv(transform_matrix)
