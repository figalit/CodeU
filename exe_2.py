class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count

	def print_(self):
		current = self.head
		while current:
			print str(current.get_data())
			current = current.get_next()


def print_kth_last(linked_list, k):
	size = linked_list.size()
	current = linked_list.head
	linked_list.print_()
	count = 0
	if k < size and k >= 0:
		while count < size-k-1:
			count += 1
			current = current.get_next()
		print str(k), str(current.get_data())
	else:
		print 'enter valid k'

def test_code():
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node4 = Node(4)
	node5 = Node(5)
	node1.set_next(node2)
	node2.set_next(node3)
	node3.set_next(node4)
	node4.set_next(node5)

	linked_list = LinkedList()
	linked_list.head = node1
	print_kth_last(linked_list, 1)

test_code()