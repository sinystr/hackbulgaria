def is_int_palindrome(number):
	array_numbers = []

	# making a list of the numbers
	while number != 0:
		array_numbers.append(number % 10)
		number //= 10

	# checking if the first half is reversed second part
	# we are using // so we can exclude the middle number, if
	# the digit count is an odd number

	for i in range(0, len(array_numbers) // 2):
		second_parameter = len(array_numbers)- i - 1
		if(array_numbers[i] != array_numbers[second_parameter]):
			return False
	return True