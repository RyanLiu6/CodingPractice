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
        left = self.lengthOfTree(root, True)
        right = self.lengthOfTree(root, False)

        return left + right

    def lengthOfTree(self, root, left):
        if not root:
            return 0
        if left:
            return 1 + self.lengthOfTree(root.left, left)
        else:
            return 1 + self.lengthOfTree(root.right, left)
