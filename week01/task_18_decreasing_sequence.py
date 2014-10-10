from task_17_increasing_sequence import is_increasing

def is_decreasing(seq):
	seq.reverse()
	return is_increasing(seq)
