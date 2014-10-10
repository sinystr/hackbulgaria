from task_4_is_prime import is_prime

def prime_number_of_devisitors(number):
	devisors_number = 1 # Starting from 1, because we check in range 1-number,
	# but the number is devisitor by itself

	#devisitors counter
	for i in range(1,number):
		if(number % i == 0):
			devisors_number += 1

	return is_prime(devisors_number)
