# Program to decompose a matrix into lower and upper triangular matrix and then compute the determinant
import numpy as np

def lu_decomposition_determinant(square_matrix: np.array):
	# dimension of the square matrix
	n = square_matrix.shape[0]

	# Create zero matrices for Lower Triangular and Upper Triangular matrix
	lower = np.zeros_like(square_matrix)
	upper = np.zeros_like(square_matrix)

	# Decomposing matrix into Upper and Lower triangular matrix
	for i in range(n):
		# Upper Triangular
		for k in range(i, n):

			# Summation of L(i, j) * U(j, k)
			sum = 0.0
			for j in range(i):
				sum += (lower[i][j] * upper[j][k])

			# Evaluating U(i, k)
			upper[i][k] = square_matrix[i][k] - sum

		# Lower Triangular
		for k in range(i, n):
			if i == k:
				lower[i][i] = 1.0 # Diagonal as 1
			else:

				# Summation of L(k, j) * U(j, i)
				sum = 0
				for j in range(i):
					sum += (lower[k][j] * upper[j][i])

				# Evaluating L(k, i)
				lower[k][i] = float((square_matrix[k][i] - sum) / upper[i][i])

	# Determinant
	return upper.diagonal().prod()


