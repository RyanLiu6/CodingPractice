# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MiscSolutions:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.L = L
        self.R = R
        self.retVal = 0

        self.sumHelper(root)
        return self.retVal

    def sumHelper(self, root):
        if not root:
            return

        currVal = root.val

        if self.L <= currVal <= self.R:
            self.retVal += currVal
        if self.L < currVal:
            self.sumHelper(root.left)
        if currVal < self.R:
            self.sumHelper(root.right)

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # Count bits individually
        retList = []
        for i in range(0, num + 1):
            retList.append(self.weight(i))

        return retList

        # Count bits by using previous
        dp = [0 for _ in range(num + 1)]

        prevStart = 1

        for i in range(1, num + 1):
            dp[i] = dp[i - prevStart] + 1
            if 2*prevStart == i:
                dp[i] = 1
                prevStart *= 2

        return dp

    def weight(self, num):
        w = 0
        while (num):
            w += 1
            num &= num - 1

        return w

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        retList = []
        left = 1

        for i in range(n):
            if i > 0:
                left *= nums[i - 1]

            retList.append(left)

        right = 1
        for i in range(n - 1, -1, -1):
            if i < (n - 1):
                right *= nums[i + 1]

            retList[i] *= right

        return retList
