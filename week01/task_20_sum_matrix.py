def sum_matrix(matrix):
	matrix_sum = 0
	for i in matrix:
		matrix_sum += sum(i)
	return matrix_sum
