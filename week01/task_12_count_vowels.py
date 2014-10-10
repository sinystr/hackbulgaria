# universal function for finding the summ of apearances 
# of members of array of characters in a string
def count_characters(str, characters):
	sum_vowels = 0
	for i in characters + characters.upper():
		sum_vowels += str.count(i)

	return sum_vowels

def count_vowels(str):
	return count_characters(str, "aeioyu")
