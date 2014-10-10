def sum_of_all_devisors(number):
	devisors_sum = 0

	#Checking numbers from 1 to the number, for devisors,
	#and adding every found devisor to devisors sum
	for i in range(1,number):
		if(number % i == 0):
			devisors_sum += i

	return devisors_sum	+ number #the number itself is devisor too																																																																																																																																											
