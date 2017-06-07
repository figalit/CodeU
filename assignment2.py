class Node(object):
	def __init__(self, data=None, left_key=None, right_key=None):
		self.data = data
		self.right_key = left_key
		self.left_key = right_key

	def get_left(self):
		return self.left_key

	def get_right(self):
		return self.right_key

	def get_data(self):
		return self.data

class BinaryTree(object):
	def __init__(self, root=None):
		self.root = root

	def insert(self, node, goal_parent, add_on_left):
		# traverse to find the goal_parent and add the node there on left or right
		parent = self.find_node(self.root, goal_parent)
		if add_on_left:
			parent.left_key = node
		else:
			parent.right_key = node
	
	def find_node(self, root_node, goal_parent):
		if root_node != None:
			if root_node == goal_parent:
				return root_node
			return (self.find_node(root_node.left_key, goal_parent) 
				or self.find_node(root_node.right_key, goal_parent))


def inorder_traversal(root_node):
	if root_node != None:
		inorder_traversal(root_node.get_left())
		print root_node.get_data()	
		inorder_traversal(root_node.get_right()) 

# FIRST QUESTION
def print_ancestors(root_node, goal_node):
	if root_node ==  None:
		return False

	if goal_node == root_node:
		return True

	if (print_ancestors(root_node.left_key, goal_node) 
		or print_ancestors(root_node.right_key, goal_node)):
		print root_node.data
		return True

	return False
	
# SECOND QUESTION 
def lowest_common_ancestor(root, first_node, second_node):
	# first make sure these two nodes exist in the tree
	if helper_find_on_subtree(root, first_node) == False or helper_find_on_subtree(root, second_node) == False:
		return None # which means there is error with input(does not exist)
	return helper_lowest_common_ancestor(root, first_node, second_node)

def helper_lowest_common_ancestor(root, first_node, second_node):
	# check if they're both on same subtree
	# the task becomes finding the root of the subtree where they are in different parts of it
	if root == None or root == first_node or root == second_node:
		return root

	first_on_left = helper_find_on_subtree(root.left_key, first_node)
	second_on_left = helper_find_on_subtree(root.left_key, second_node)
	if first_on_left != second_on_left:
		return root

	where_next = None
	if first_on_left:
		where_next = root.left_key
	else:
		where_next = root.right_key
	return helper_lowest_common_ancestor(where_next, first_node, second_node)

def helper_find_on_subtree(root, node_to_find):
	if root == None:
		return False

	if root == node_to_find:
		return True
	return helper_find_on_subtree(root.left_key, node_to_find) or helper_find_on_subtree(root.right_key, node_to_find)

def test_program():
	# create a tree
	node1 = Node(1)
	node3 = Node(3)
	node5 = Node(5)
	node9 = Node(9)
	node14 = Node(14)
	node16 = Node(16)
	node18 = Node(18)
	node19 = Node(19)
	
	binary_tree = BinaryTree()
	binary_tree.root = node16

	binary_tree.insert(node9, node16, True)
	binary_tree.insert(node3, node9, True)
	binary_tree.insert(node14, node9, False)
	binary_tree.insert(node1, node3, True)
	binary_tree.insert(node5, node3, False)
	binary_tree.insert(node18, node16, False)
	binary_tree.insert(node19, node18, False)
	# inorder_traversal(binary_tree.root)

	print_ancestors(binary_tree.root, node5)

	print str(lowest_common_ancestor(binary_tree.root, node5, node14).data)
	print str(lowest_common_ancestor(binary_tree.root, node3, node9).data)
	print str(lowest_common_ancestor(binary_tree.root, node1, node18).data)

test_program()
