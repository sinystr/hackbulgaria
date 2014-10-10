def nan_expand(n):
	nan_string = ""

	#if n == 0, we return the empty string
	if(n == 0):
		return nan_string
	# for adding "Not a " n times
	for i in range(0,n):
		nan_string += "Not a "		
	# and we close with just NaN, so the string make sense
	nan_string += "NaN"

	return nan_string
