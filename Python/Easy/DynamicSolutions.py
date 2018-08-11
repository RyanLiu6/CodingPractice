class DPSolutions:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        Input: 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

        Input: 3
        Output: 3
        Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
        """
        self.stairs = []
        self.prepStairs(n)

        return self.stairs[n]

    def prepStairs(self, n):
        self.stairs.append(0)
        self.stairs.append(1)
        self.stairs.append(2)

        for i in range(3, n + 1):
            self.stairs.append(self.stairs[i - 1] + self.stairs[i - 2])

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Input: [7,1,5,3,6,4]
        Output: 5
        """
        # Buy and then sell
        if not prices:
            return 0

        buy = prices[0]
        profit = 0

        for p in prices:
            buy = min(buy, p)
            curr = p - buy
            profit = max(profit, curr)

        return profit

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
        """
        if not nums:
            return 0

        maxSum = nums[0]
        currSum = 0
        print(nums)

        for num in nums:
            currSum += num
            print(currSum, end=", ")
            maxSum = max(maxSum, currSum)
            print(maxSum, end=", ")
            currSum = max(currSum, 0)
            print(currSum)

        return maxSum

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
        """
        # With space
        n = len(nums)
        if not nums:
            return 0
        if n < 2:
            return nums[0]

        robList = []
        robList.append(nums[0])
        robList.append(max(nums[0], nums[1]))

        for i in range(2, n):
            robList.append(max(robList[i - 2] + nums[i], robList[i - 1]))

        return robList[n - 1]

        # Without space
