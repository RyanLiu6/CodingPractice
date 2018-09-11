# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TGSolutions:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.sameHelper(p, q)

    def sameHelper(self, p, q):
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False

        if p.val == q.val:
            left = self.sameHelper(p.left, q.left)
            right = self.sameHelper(p.right, q.right)

            return left and right
        else:
            return False

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        retArr = []
        if not root:
            return retArr

        self.pathHelper(retArr, root, "")

        return retArr

    def pathHelper(self, retArr, root, path):
        if not root.left and not root.right:
            retArr.append(path + str(root.val))
            return

        path += str(root.val) + "->"
        if root.left:
            self.pathHelper(retArr, root.left, path)
        if root.right:
            self.pathHelper(retArr, root.right, path)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diam = 0
        self.depthOfTree(root)

        return self.diam

    def depthOfTree(self, root):
        if not root:
            return 0

        left = self.depthOfTree(root.left)
        right = self.depthOfTree(root.right)

        self.diam = max(self.diam, left + right)
        return 1 + max(left, right)

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
