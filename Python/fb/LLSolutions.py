# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LLSolutions:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        Result is preorder LL (root, left, right)
        """
        self.flatHelper(root)

    def flatHelper(self, root):
        if not root:
            return
        self.flatHelper(root.left)
        self.flatHelper(root.right)
        
        right = root.right
        if root.left:
            root.right = root.left
            root.left = None

            while root.right:
                root = root.right

            root.right = right
