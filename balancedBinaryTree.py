'''
Given a binary tree, detrmine if it is heght-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and the right subtrees of every node differ in height by no more than 1.
example 1:
Goven the folosing tree [3,9,20,null,null, 15, 7]
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode):
        cache = {}
        #check the height
        def getHeight(n):
            if n == None:
                return 0
            #return 1 + max(getHeight(n.left). getHeight(n.right))
            if n not in cache:
                cache[n] = 1 + max(getHeight(n.left), getHeight(n.right))
            return cache[n]

        # Test if the root is balanced
        # def balanced(root):
        #     if root is None:
        #         return True
        if root is None:
            return True
        l_height = getHeight(root.left)
        r_height = getHeight(root.right)   
        #return abs(l_height - r_height) <= 1 and balanced(root.left) and balanced(root.right) #if the right and left are balanced then the tree must be balanced
        return abs(l_height - r_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) #if the right and left are balanced then the tree must be balanced

        #return balanced(root)
