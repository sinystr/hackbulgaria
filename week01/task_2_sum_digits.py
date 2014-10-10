def make_valid(number):
	if number < 0:
		return number * (-1)
	elif(number >= 0):
		return number
	else:
		die("Something went wrong!")

def sum_of_digits(number):
	#Removing the sign of the number
	number = make_valid(number)

	#Getting every digit, one by one and adding it to sum_digits
	sum_digits = 0
	while(number != 0):
		sum_digits += number % 10
		number //= 10

	return sum_digits
