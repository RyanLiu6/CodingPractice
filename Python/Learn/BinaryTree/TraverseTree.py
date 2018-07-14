class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TraverseSolutions:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        retArr = []
        self.preHelper(root, retArr)
        return retArr

    def preHelper(self, root, retArr):
        if not root:
            return

        retArr.append(root.val)
        self.preHelper(root.left, retArr)
        self.preHelper(root.right, retArr)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        retArr = []
        self.inHelper(root, retArr)
        return retArr

    def inHelper(self, root, retArr):
        if not root:
            return

        self.inHelper(root.left, retArr)
        retArr.append(root.val)
        self.inHelper(root.right, retArr)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        retArr = []
        self.postHelper(root, retArr)
        return retArr

    def postHelper(self, root, retArr):
        if not root:
            return

        self.postHelper(root.left, retArr)
        self.postHelper(root.right, retArr)
        retArr.append(root.val)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Recursive 1
        # retArr = []
        # self.levHelper(root, retArr, 0)
        # return retArr

        # Recursive 2
        if not root:
            return []

        retArr = []
        queue = [root]
        self.levHelper(retArr, queue)
        return retArr

    def levHelper(self, retArr, queue):
        if not queue:
            return

        n = len(queue)
        levArr = []
        for i in range(n):
            currNode = queue.pop(0)
            levArr.append(currNode.val)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

        retArr.append(levArr)
        self.levHelper(retArr, queue)

        return retArr

    # def levHelper(self, curr, retArr, level):
    #     if not curr:
    #         return
    #
    #     if len(retArr) == level:
    #         retArr.append([])
    #
    #     retArr[level].append[curr.val]
    #
    #     self.levHelper(curr.left, retArr, level+1)
    #     self.levHelper(curr.right, retArr, level+1)
