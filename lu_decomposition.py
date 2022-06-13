# Program to decompose a matrix into lower and upper triangular matrix and then compute the determinant

def lu_decomposition(square_matrix):
	# dimension of the square matrix
	n = len(square_matrix[0])

	# Create zero matrices for Lower Triangular and Upper Triangular matrix
	lower = [[0.0 for x in range(n)] for y in range(n)]
	upper = [[0.0 for x in range(n)] for y in range(n)]

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
	determinant = 1
	for d in range(n):
		determinant *= upper[d][d] 	# product of the diagonals

	# Print the results
	print("Lower Triangular\t\t\tUpper Triangular")

	# Do some formatting for visualization
	lens = []
	for col in zip(*lower):
		lens.append(max([len(str(v)) for v in col]))
	format = "  ".join(["{:<" + str(l) + "}" for l in lens])

	for i in range(n):

		row_l = lower[i]
		row_u = upper[i]

		print(format.format(*row_l), end="\t\t")
		print("", end="\t\t")
		print(format.format(*row_u), end="\t\t")
		print("", end="\t\t")
		print("")

	print()
	print(f"Determinant: {determinant} ")


# input: square matrix for computing the determinant
matrix = [	[2,  -1, -2],
			[-4,  6,  3],
			[-4, -2,  8]]

lu_decomposition(matrix)


