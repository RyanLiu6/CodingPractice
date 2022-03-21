class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class RecurseSolutions:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
            1
           / \
          2   2
         / \ / \
        3  4 4  3
        """
        if not root:
            return True

        return self.symHelper(root.left, root.right)

    def symHelper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.val == right.val:
            i = self.symHelper(left.left, right.right)
            j = self.symHelper(left.right, right.left)

            return i and j
        else:
            return False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.sumHelper(root, 0, sum)

    def sumHelper(self, node, currVal, target):
        if not node:
            return False

        currVal += node.val

        if currVal == target and (not node.left and not node.right):
            return True

        left = self.sumHelper(node.left, currVal, target)
        right = self.sumHelper(node.right, currVal, target)

        return left or right
