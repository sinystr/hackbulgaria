def contains_digit(number, digit):
	# Checking every single number 
	while number > 0:
		if(number % 10 == digit):
			return True #returning true after first found
		number //= 10
		
	return False