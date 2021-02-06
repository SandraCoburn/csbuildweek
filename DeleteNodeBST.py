def deleteNode(root, key):
	if not root: 
		return root
	if root.val > key: 
		root.left = deleteNode(root.left, key) 
	elif root.val < key: 
		root.right= deleteNode(root.right, key)
	else:
		if not root.right:
			return root.left	
		if not root.left:
			return root.right
		temp_val = root.right
		mini_val = temp_val.val
		while temp_val.left:
			temp_val = temp_val.left
			mini_val = temp_val.val
		root.right = deleteNode(root.right,root.val)
	return root

def deleteNode(root, key):
	if not root: 
		return root
	if root.val > key: 
		root.left = deleteNode(root.left, key) 
	elif root.val < key: 
		root.right= deleteNode(root.right, key)
	else:
		if not root.right:
			return root.left	
		if not root.left:
			return root.right
		temp_val = root.right
		mini_val = temp_val.val
		while temp_val.left:
			temp_val = temp_val.left
			mini_val = temp_val.val
		root.right = deleteNode(root.right,root.val)
	return root