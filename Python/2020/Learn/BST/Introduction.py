# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class IntroSoln:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, None, None)

    def isValid(self, root, min, max):
        if not root:
            return True

        if min != None and root.val <= min:
            return False

        if max != None and max <= root.val:
            return False

        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)
