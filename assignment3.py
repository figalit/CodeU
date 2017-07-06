class Dictionary(object):
	def __init__(self, dictionary=None):
		self.dictionary = []

	def insert_words(self, word_list):
		self.dictionary = word_list

	def is_word(self, string):
		return (string in self.dictionary)

	def is_prefix(self, string):
		for word in self.dictionary:
			if len(word) >= len(string) and word[0:len(string)] == string:
				return True
		return False


result_set = []
def solution(n_rows, n_columns, matrix, dict_object):
	word_sofar = ''
	for i in range(n_rows):
		for j in range(n_columns):
			visited = []
			find_word_for_cell(n_rows, n_columns, matrix, dict_object, i, j, word_sofar, visited)

	print(result_set)


def find_word_for_cell(n_rows, n_columns, matrix, dict, row_number, col_number, word_sofar, visited ):\

	word_sofar = word_sofar + matrix[row_number][col_number]

	if(dict.is_word(word_sofar)):
		# print(word_sofar)
		result_set.append(word_sofar)

	if(not dict.is_prefix(word_sofar)):
		return

	visited.append([row_number,col_number])

	# left up
	if(row_number-1 >= 0 and col_number -1 >=0 and [row_number-1,col_number-1] not in visited):
		find_word_for_cell(n_rows, n_columns, matrix, dict, row_number-1, col_number-1, word_sofar, visited)
	# middle up
	if(row_number-1 >= 0 and [row_number-1,col_number] not in visited):
		find_word_for_cell(n_rows, n_columns, matrix, dict, row_number-1, col_number, word_sofar, visited)
	# right up
	if(row_number-1 >= 0 and col_number +1 < n_columns and [row_number-1,col_number+1] not in visited):
		find_word_for_cell(n_rows, n_columns, matrix, dict, row_number-1, col_number+1, word_sofar, visited)
	# left middle
	if( col_number -1 >=0 and [row_number,col_number-1] not in visited):
		find_word_for_cell(n_rows, n_columns, matrix, dict, row_number, col_number-1, word_sofar, visited)
	# right middle
	if(col_number +1 < n_columns and [row_number,col_number+1] not in visited):
		find_word_for_cell(n_rows, n_columns, matrix, dict, row_number, col_number+1, word_sofar, visited)
	# left down
	if(row_number+1 < n_rows and col_number -1 >=0 and [row_number+1,col_number-1] not in visited):
		find_word_for_cell(n_rows, n_columns, matrix, dict, row_number+1, col_number-1, word_sofar, visited)
	# middle down
	if(row_number+1 < n_rows and [row_number+1,col_number] not in visited):
		find_word_for_cell(n_rows, n_columns, matrix, dict, row_number+1, col_number, word_sofar, visited)
	# right down
	if(row_number+1 < n_rows and col_number +1 < n_columns and [row_number+1,col_number+1] not in visited):
		find_word_for_cell(n_rows, n_columns, matrix, dict, row_number+1, col_number+1, word_sofar, visited)


dictionary = Dictionary()
dictionary.insert_words(['CAR', 'CARD', 'CART', 'CAT'])
matrix = [['A', 'A', 'R'],['T', 'C', 'D']]

solution(2, 3, matrix, dictionary)
