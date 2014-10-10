def list_to_number(number):
	string = []
	while len(number) > 0:
		string += str(number.pop(0))
	string = ''.join(string)
	
	return int(string)
