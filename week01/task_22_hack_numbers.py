from task_7_is_int_polyndrome import is_int_palindrome

#function that checks if a number is a "hack number"
def is_a_hack_number(number):
	binary_number = "{0:b}".format(number)
	if(is_int_palindrome(int(binary_number)) and (binary_number.count('1') % 2 == 1)):
		return True
	return False

def next_hack(n):
	n += 1
	#starting to search for the next hack number
	while not is_a_hack_number(n):
		n += 1
	
	return n

