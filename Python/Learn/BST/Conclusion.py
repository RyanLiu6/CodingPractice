import heapq

class KthLargest:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.minHeap = []

        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif self.minHeap[0] < val:
            heapq.heappushpop(self.minHeap, val)

        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left
        return root

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.result = True
        self.balanceHelper(root)
        return self.result

    def balanceHelper(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        left = self.balanceHelper(root.left)
        right = self.balanceHelper(root.right)

        if abs(left - right) > 1:
            self.result = False

        return 1 + max(left, right)

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def sortedHelper(start, end):
            if end < start:
                return None

            mid = (start + end) // 2
            root = TreeNode(nums[mid])

            root.left = sortedHelper(start, mid - 1)
            root.right = sortedHelper(mid + 1, end)

            return root

        return sortedHelper(0, len(nums) - 1)
