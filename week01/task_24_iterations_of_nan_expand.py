def iterations_of_nan_expand(expanded):
	if(expanded.count("Not a ") * 6 != len(expanded) - 3):
		return False
	return expanded.count("Not a ")
