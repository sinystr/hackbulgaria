def is_increasing(seq):
	for i in range(0,len(seq) - 1):
		if(seq[i] >= seq[i + 1]):
			return False
	return True
