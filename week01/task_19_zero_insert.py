from task_15_list_to_number import list_to_number	 
from task_14_number_to_list import number_to_list	 

def zero_insert(n):
	list_n = number_to_list(n)
	for i in range(0, len(list_n) - 1):
		if(list_n[i] == list_n[i + 1]):
			list_n.insert(i+1,0)

	return list_to_number(list_n)
