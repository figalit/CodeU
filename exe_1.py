import sys

def findPermutations(str1, str2):
	str1 = str1.lower()
	str2 = str2.lower()

	letters_and_frequencies_1 = make_letters_and_frequencies(str1)
	letters_and_frequencies_2 = make_letters_and_frequencies(str2)
	return compare_dicts(letters_and_frequencies_1, letters_and_frequencies_2)

def make_letters_and_frequencies(string):
	lf = {}
	for char in string:
		if char in lf:
			lf[char] += 1
		else:
			lf[char] = 1
	return lf

def compare_dicts(dict1, dict2):
	for char in dict1.keys():
		if char not in dict2.keys():
			return False
		else:
			if dict2[char] != dict1[char]:
				return False
	for char in dict2.keys():
		if char not in dict1.keys():
			return False
		else:
			if dict2[char] != dict1[char]:
				return False
	
	return True

print findPermutations(sys.argv[1], sys.argv[2])
