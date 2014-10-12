
def magic_square(matrix):

    # Finding the main number
    magic_number = sum(matrix[0])

    # Checking the rows

    for i in matrix:
        if sum(i) != magic_number:
            return False

    # Chechking the columns
    for i in range(0, len(matrix)):
        current_sum = 0
        for k in range(0, len(matrix)):
            current_sum += matrix[i][k]

        if current_sum != magic_number:
            return False

    # Checking the main diagonal
    current_sum = 0
    for i in range(0, len(matrix)):
        current_sum += matrix[i][i]

    if current_sum != magic_number:
        return False

    # Checking the other diagonal
    current_sum = 0
    for i in range(0, len(matrix)):
        current_sum += matrix[i][len(matrix)-i-1]

    if current_sum != magic_number:
            return False

    return True

print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
