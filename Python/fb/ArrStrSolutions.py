class ArrStrSolutions:
    def validPalindromeII(self, s):
        """
        :type s: str
        :rtype: bool
        Is it a Palindrome if you can remove up to a single character?
        """
        n = len(s)

        i, j = 0, n - 1

        while i < j:
            if s[i] != s[j]:
                first = s[i:j]
                second = s[i + 1:j + 1]

                return first == first[::-1] or second == second[::-1]
            i += 1
            j -= 1
        return True

    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # DP Solution O(n^2)
        n = len(nums)
        maxLength = 0

        for i in range(n):
            for j in range(n):
                if i <= j:
                    curr = nums[i:j + 1]
                    if sum(curr) == k:
                        maxLength = max(maxLength, len(curr))

        return maxLength

        # O(n)
        n = len(nums)
        cSum = maxLength = 0
        numDict = {}

        for i in range(n):
            cSum += nums[i]

            if cSum == k:
                maxLength = i + 1
            elif numDict.get(cSum - k, -1) != -1:
                maxLength = max(maxLength, i - numDict[cSum - k])

            if not cSum in numDict:
                numDict[cSum] = i

        return maxLength

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # O(n^2)
        water = 0
        n = len(height)

        for i in range(1, n - 1):
            maxLeft = maxRight = 0
            for j in range(i, -1, -1):
                maxLeft = max(maxLeft, height[j])
            for j in range(i, n):
                maxRight = max(maxRight, height[j])
            print(i, maxLeft, maxRight)
            water += min(maxLeft, maxRight) - height[i]

        return water
