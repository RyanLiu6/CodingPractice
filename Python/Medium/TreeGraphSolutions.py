class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeGraphSolutions:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        [
          [3],
          [20,9],
          [10,25,15,7]
        ]
        """
        retArr = []
        if not root:
            return retArr

        queue = [root]
        # 0 is left to right
        # 1 is right to left
        self.whichOrder = 0

        self.zzHelper(retArr, queue)
        return retArr

    def zzHelper(self, retArr, queue):
        n = len(queue)
        if n == 0:
            return

        levArr = []
        for i in range(n):
            currNode = queue.pop(0)
            levArr.append(currNode.val)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

        if self.whichOrder % 2:
            retArr.append(levArr[::-1])
        else:
            retArr.append(levArr)

        self.whichOrder += 1
        self.whichOrder %= 2
        self.zzHelper(retArr, queue)

        return retArr

    def buildTree(self, preOrder, inOrder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inDict = {}
        for key, value in enumerate(inOrder):
            inDict[value] = key

        def inPreHelper(preStart, preEnd, inStart, inEnd):
            if preEnd < preStart or inEnd < inStart:
                return None

            curr = preOrder[preStart]
            pos = inDict[curr]

            node = TreeNode(curr)
            node.left = inPreHelper(preStart + 1, preStart + 1 + (pos - 1 - inStart), inStart, pos - 1)
            node.right = inPreHelper(preStart + 1 + (pos - inStart), preEnd, pos + 1, inEnd)

            return Node

        return inPreHelper(0, len(preOrder) - 1, 0, len(inOrder) - 1)

    def connect(self, root):
        """
        :type root: TreeNode
        :rtype: None
        """
        if not root:
            return

        self.conHelper(root, None)

    def conHelper(self, left, right):
        if left:
            left.next = right
            self.conHelper(left.left, left.right)
            if right:
                self.conHelper(left.right, right.left)
            else:
                self.conHelper(left.right, None)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Count nodes before progressing
        count = self.countNodes(root.left)

        if k <= count:
            return self.kthSmallest(root.left, k)
        elif k > count + 1:
            return self.kthSmallest(root.right, k - 1 - count)

        return root.val

        # InOrder Traversal
        count = []
        self.smallestHelper(root, count)
        return count[k - 1]

    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def smallestHelper(self, root, count):
        if not node:
            return

        self.smallestHelper(root.left, count)
        count.append(root.val)
        self.smallestHelper(root.right, count)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
