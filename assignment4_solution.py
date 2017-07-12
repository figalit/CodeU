##################### Solution explanation ##########################################
# The idea is to iterate through all the matrix and create a set of 'trues', 
# which could be rightfully be avoided (but hasn't been for ease of understanding).
# For each true-unvisited, we make it visited, and then look into 
# it's neighbours and neighbours' neighbours or the belong_to's.
# Only after this is over, we increment the result counter.
####################################################################################


def make_belong_set(item, trues):
	# need to check if items at [i-1, j], [i, j-1], [i+1, j], [i, j+1] are in trues
	i = item[0]
	j = item[1]
	belong_set = []
	if (i-1, j) in trues.keys() and trues[(i-1, j)] == 'not_visited':
		belong_set.append((i-1, j))
	if (i, j-1) in trues.keys() and trues[(i, j-1)] == 'not_visited':
		belong_set.append((i, j-1))
	if (i+1, j) in trues.keys() and trues[(i+1, j)] == 'not_visited':
		belong_set.append((i+1, j))
	if (i, j+1) in trues.keys() and trues[(i, j+1)] == 'not_visited':
		belong_set.append((i, j+1))
	return belong_set

def find_number_of_islands(row_no, col_no, matrix):
	result_count = 0
	# key: 'True' coordinates in matrix
	# value: 'visited' or 'belongs_to' or 'not_visited'
	trues = {}

	# fill trues dict
	for i in range(row_no):
		for j in range(col_no):
			if matrix[i][j]:
				trues[(i, j)] = 'not_visited'

	# go through trues, and for each not_visited, find its belongs_to set. 
	# then for each of belongs_to iterate to find further on, until no belongs_to are left
	# repeat
	for item in trues.keys():
		# item is an [i, j] list
		if trues[item] == 'not_visited':
			trues[item] = 'visited'
			belong_set = make_belong_set(item, trues)
			handle_belongs(belong_set, trues)
			result_count += 1

	print result_count

def handle_belongs(belong_set, trues):
	# for each item in belong_set
	# 	make it visited, 
	#	make its neighbours that are in trues as belongs_to
	# repeat for as long as belong_set is not empty
	for item in belong_set:
		trues[item] = 'visited'
		belong_set_ = make_belong_set(item, trues)
		if not not belong_set:
			handle_belongs(belong_set_, trues)

# testing
row = 4
column = 4 
matrix=[[True, True, False, True], 
		[True, False, False, False], 
		[False, False, True, False],
		[True, False, False, True]]

find_number_of_islands(row, column, matrix)