class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        treeDepth = 1

        for child in root.children:
            treeDepth = max(treeDepth, 1 + self.maxDepth(child))

        return treeDepth
