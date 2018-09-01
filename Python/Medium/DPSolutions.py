class DPSolutions:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Recursive Solution
        # if not nums:
        #     return False
        #
        # return self.jumpHelper(nums, 0, nums[0], len(nums) - 1)

        # DP Solution (?)
        n = len(nums)
        maxJump = 0

        for i in range(n):
            if i > maxJump:
                return False
            maxJump = max(maxJump, i + nums[i])

        return True

    def jumpHelper(self, nums, index, maxJump, target):
        if nums[index] + maxJump >= target:
            return True

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Recursive Solution
        self.row = n
        self.col = m

        return self.pathHelper(0, 0)

        # DP Solution
        DP = [[1 for x in range(m)] for y in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                DP[i][j] = DP[i - 1][j] + DP[i][j - 1]

        return DP[n - 1][m - 1]

    def pathHelper(self, i, j):
        if i < self.row and j < self.col:
            if i == self.row - 1 and j == self.col - 1:
                return 1
            else:
                down = self.pathHelper(i + 1, j)
                right = self.pathHelper(i, j + 1)
                return down + right
        else:
            return 0

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Greedy Solution
        count = 0
        coins.sort()
        for i in range(len(coins) - 1, -1, -1):
            while amount >= coins[i]:
                amount -= coins[i]
                count += 1

        if amount == 0:
            return count
        else:
            return -1

        # DP Solution
        n = len(coins)
        DP = [0 for _ in range(amount + 1)]


    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP Solution O(n^2)
        if not nums:
            return 0

        retInt = 1
        n = len(nums)
        DP = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    DP[i] = max(DP[i], DP[j] + 1)
            retInt = max(retInt, DP[i])

        return retInt
