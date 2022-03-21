from collections import deque


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        retArr = []

        def preHelper(root):
            if not root:
                return

            retArr.append(root.val)
            for i in range(len(root.children)):
                preHelper(root.children[i])

        preHelper(root)
        return retArr

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        retArr = []

        def postHelper(root):
            if not root:
                return

            for i in range(len(root.children)):
                postHelper(root.children[i])

            retArr.append(root.val)

        postHelper(root)
        return retArr

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        nodeArr = []
        if not root:
            return nodeArr

        queue = deque([root])

        def levHelper():
            if not queue:
                return

            levArr = []

            for i in range(len(queue)):
                curr = queue.popleft()
                levArr.append(curr.val)

                if curr.children:
                    for child in curr.children:
                        queue.append(child)

            nodeArr.append(levArr)
            levHelper()

        levHelper()
        return nodeArr
