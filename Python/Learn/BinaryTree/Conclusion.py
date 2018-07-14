from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ConcluSolutions:
    def buildInPost(self, inOrder, postOrder):
        """
        :type inOrder: List[int]
        :type postOrder: List[int]
        :rtype: TreeNode
        """
        # # Solution 1
        # if not inOrder or not postOrder:
        #     return None
        #
        # if len(inOrder) == 1 and len(postOrder) == 1:
        #     return TreeNode(inOrder[0])
        #
        # # find the pos of postOrder[end] in inOrder
        # data = postOrder[len(postOrder) - 1]
        # pos = inOrder.index(data)
        #
        # node = TreeNode(data)
        #
        # inLeft = inOrder[:pos]
        # inRight = inOrder[pos + 1:]
        # postLeft = postOrder[:len(inLeft)]
        # postRight = postOrder[len(inLeft):len(postOrder) - 1]
        #
        # node.left = self.buildTree(inLeft, postLeft)
        # node.right = self.buildTree(inRight, postRight)
        #
        # return node

        # Solution 2
        inDict = {}

        for i in range(len(inOrder)):
            inDict[inOrder[i]] = i

        def InPostHelper(inStart, inEnd, postStart, postEnd):
            if inStart > inEnd or postStart > postEnd:
                return None

            data = postOrder[postEnd]
            pos = inDict[data]

            node = TreeNode(data)

            node.left = InPostHelper(inStart, pos - 1, postStart, postStart + (pos - 1 - inStart))
            node.right = InPostHelper(pos + 1, inEnd, postStart + (pos - inStart), postEnd - 1)

            return node

        return InPostHelper(0, len(inOrder) - 1, 0, len(postOrder) - 1)

    def buildPreIn(self, preOrder, inOrder):
        """
        :type preOrder: List[int]
        :type inOrder: List[int]
        :rtype: TreeNode
        """
        inDict = {}

        for i in range(len(inOrder)):
            inDict[inOrder[i]] = i

        def InPreHelper(inStart, inEnd, preStart, preEnd):
            if inStart > inEnd or preStart > preEnd:
                return None

            data = preOrder[preStart]
            pos = inDict[data]

            node = TreeNode(data)

            node.left = InPreHelper(inStart, pos - 1, preStart + 1, preStart + 1 + (pos - 1 - inStart))
            node.right = InPreHelper(pos + 1, inEnd, preStart + 1 + (pos - inStart), preEnd)

            return node

        return InPreHelper(0, len(inOrder) - 1, 0, len(preOrder) - 1)

    def serialize(self, root):
        """
        Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = deque([root])
        nodeStr = ""

        while queue:
            node = queue.popleft()
            if not node:
                nodeStr += "~ "
                continue

            nodeStr += str(node.val) + " "

            queue.append(node.left)
            queue.append(node.right)

        return nodeStr

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        treeData = data.split()
        root = TreeNode(int(treeData[0]))

        queue = deque([root])

        i = 1
        while queue:
            node = queue.popleft()
            if treeData[i] != "~":
                left = TreeNode(int(treeData[i]))
                node.left = left
                queue.append(left)

            i += 1

            if treeData[i] != "~":
                right = TreeNode(int(treeData[i]))
                node.right = right
                queue.append(right)

            i += 1

        return root
