def number_to_list(number):
	list_numbers = []
	while number > 0:
		list_numbers.append(number % 10)
		number //= 10
			
	list_numbers.reverse()
	
	return list_numbers
