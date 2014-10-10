def biggest_difference(arr):
	biggest_difference_number = 0
	for i in range(0,len(arr)):
		for k in range(i + 1, len(arr)):
			#checking every possible difference and finding the biggest
			if((arr[i] - arr[k]) < biggest_difference_number):
				biggest_difference_number = arr[i] - arr[k]
			if((arr[k] - arr[i]) < biggest_difference_number):
				biggest_difference_number = arr[k] - arr[i]

	return biggest_difference_number
