# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


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
        retArr = []

        if not root:
            return retArr

        self.min = 0
        self.max = 0

        bucket = {}
        queue = []
        cols = []

        queue.append(root)
        cols.append(0)

        self.voHelper(bucket, queue, cols)

        for i in range(self.min, self.max + 1):
            retArr.append(bucket[i])

        return retArr

    def voHelper(self, bucket, queue, cols):
        while queue:
            node = queue.pop(0)
            curr = cols.pop(0)

            if not curr in bucket:
                bucket[curr] = []

            bucket[curr].append(node.val)

            if node.left:
                queue.append(node.left)
                cols.append(curr - 1)
                self.min = min(self.min, curr - 1)

            if node.right:
                queue.append(node.right)
                cols.append(curr + 1)
                self.max = max(self.max, curr + 1)

    def buildTree(self, preOrder, inOrder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
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

    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        dummy = Node(0, None, None)
        self.prev = dummy

        self.doubleHelper(root)

        # Connect head and tail
        self.prev.right = dummy.right
        dummy.right.left = self.prev

        return dummy.right

    def doubleHelper(self, root):
        if not root:
            return

        self.doubleHelper(root.left)

        self.prev.right = root
        root.left = self.prev
        self.prev = root

        self.doubleHelper(root.right)

    def cloneGraph(self, node):
        """
        :type root: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        self.nodeDict = {}
        return self.cloneHelper(node)

    def cloneHelper(self, root):
        if not root:
            return None

        if root.label in self.nodeDict:
            return self.nodeDict[root.label]

        clone = UndirectedGraphNode(root.label)
        self.nodeDict[clone.label] = clone

        for neighbour in root.neighbors:
            clone.neighbors.append(self.cloneHelper(neighbour))

        return clone
