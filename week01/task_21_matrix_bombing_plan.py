from task_20_sum_matrix import sum_matrix

def damage(element,damage):
	if element > damage:
		return damage
	return element

def find_sum_of_neighbours(matrix,n,m):
	full_damage = 0
	matrix_n = len(matrix)-1
	matrix_m = len(matrix[0])-1

	if(n == 0):
		if(m == 0):
			full_damage += damage(matrix[0][1], matrix[n][m])
			full_damage += damage(matrix[1][1], matrix[n][m])
			full_damage += damage(matrix[1][0], matrix[n][m])
			return full_damage

		if(m == matrix_m):
			full_damage += damage(matrix[0][m-1], matrix[n][m])
			full_damage += damage(matrix[1][m-1], matrix[n][m])
			full_damage += damage(matrix[1][m], matrix[n][m])
			return full_damage

		full_damage += damage(matrix[0][m-1], matrix[n][m])
		full_damage += damage(matrix[0][m+1], matrix[n][m])
		full_damage += damage(matrix[1][m-1], matrix[n][m])
		full_damage += damage(matrix[1][m], matrix[n][m])
		full_damage += damage(matrix[1][m+1], matrix[n][m])
		return full_damage	

	if(m == 0):
		if(n == matrix_n):
			full_damage += damage(matrix[n][m+1], matrix[n][m])
			full_damage += damage(matrix[n-1][m], matrix[n][m])
			full_damage += damage(matrix[n-1][m+1], matrix[n][m])
			return full_damage

		full_damage += damage(matrix[n-1][m+1], matrix[n][m])
		full_damage += damage(matrix[n+1][m+1], matrix[n][m])
		full_damage += damage(matrix[n][m+1], matrix[n][m])
		full_damage += damage(matrix[n-1][m], matrix[n][m])
		full_damage += damage(matrix[n+1][m], matrix[n][m])
		return full_damage

	if(n == matrix_n):
		if(m == matrix_m):
			full_damage += damage(matrix[n-1][m], matrix[n][m])
			full_damage += damage(matrix[n-1][m-1], matrix[n][m])
			full_damage += damage(matrix[n][m-1], matrix[n][m])
			return full_damage


		full_damage += damage(matrix[n][m-1], matrix[n][m])
		full_damage += damage(matrix[n][m+1], matrix[n][m])
		full_damage += damage(matrix[n-1][m-1], matrix[n][m])
		full_damage += damage(matrix[n-1][m], matrix[n][m])
		full_damage += damage(matrix[n-1][m+1], matrix[n][m])
		return full_damage	

	if(m == matrix_m):
		full_damage += damage(matrix[n-1][m], matrix[n][m])
		full_damage += damage(matrix[n+1][m], matrix[n][m])
		full_damage += damage(matrix[n-1][m-1], matrix[n][m])
		full_damage += damage(matrix[n][m-1], matrix[n][m])
		full_damage += damage(matrix[n+1][m-1], matrix[n][m])
		return full_damage	

	full_damage += damage(matrix[n-1][m+1], matrix[n][m])
	full_damage += damage(matrix[n-1][m], matrix[n][m])
	full_damage += damage(matrix[n-1][m-1], matrix[n][m])
	full_damage += damage(matrix[n][m+1], matrix[n][m])
	full_damage += damage(matrix[n][m-1], matrix[n][m])	
	full_damage += damage(matrix[n+1][m-1], matrix[n][m])	
	full_damage += damage(matrix[n+1][m], matrix[n][m])	
	full_damage += damage(matrix[n+1][m+1], matrix[n][m])	
	return full_damage

def matrix_bombing_plan(matrix):
	bombing_plan_scheme = {}
	matrix_n = len(matrix)
	matrix_m = len(matrix[0])
	for i in range(0,matrix_n):
		for k in range(0,matrix_m):
			bombing_plan_scheme[(i,k)] = find_sum_of_neighbours(matrix, i, k)
	return bombing_plan_scheme

print(matrix_bombing_plan([

		[1,2,3],
		[4,5,6],
		[7,8,9]

	]))
