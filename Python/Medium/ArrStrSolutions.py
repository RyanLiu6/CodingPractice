class ArrStrSolutions:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Given array nums = [-1, 0, 1, 2, -1, -4],

        A solution set is:
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]

        Sorted = [-4, -1, -1, 0, 1, 2]
        """
        nums.sort()
        retArr = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            s, e = i + 1, n - 1
            while s < e:
                if nums[s] + nums[e] == target:
                    retArr.append([nums[i], nums[s], nums[e]])
                    s += 1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1
                elif nums[s] + nums[e] < target:
                    s += 1
                else:
                    e -= 1

        return retArr

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        zeroRows = set()
        zeroCols = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)

        for i in range(n):
            for j in range(m):
                if i in zeroRows or j in zeroCols:
                    matrix[i][j] = 0

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Given "abcabcbb", the answer is "abc", which the length is 3.
        """
        longest = 0
        if not s:
            return longest

        j = 0
        n = len(s)
        charDict = {}

        for i in range(n):
            curr = s[i]
            if curr in charDict:
                j = max(j, charDict[curr] + 1)
            longest = max(longest, i - j + 1)
            charDict[curr] = i

        return longest

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Using 2D array
        n = len(s)
        self.maxLen = 0
        self.maxPalin = ""
        
        DP = [[-1 for x in range(n)] for y in range(n)]

        for i in range(n):
            for j in range(n):
                if i <= j and DP[i][j] == -1:
                    DP[i][j] = 1
                    subStr = s[i:j + 1]
                    currLen = len(subStr)
                    if self.isPalin(subStr) and currLen > self.maxLen:
                        self.maxPalin = subStr
                        self.maxLen = currLen

        return self.maxPalin

        # Sliding Window technique
        n = len(s)
        currLen = 0
        maxPalin = ""

    def isPalin(self, string):
        return string[::-1] == string

    def isPalin(self, inputStr, start, end):
        if end < start:
            return False

        while start < end:
            if inputStr[start] != inputStr[end]:
                return False
            start += 1
            end -= 1

        return True

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        firstMin = 1 << 31
        secondMin = 1 << 31

        for num in nums:
            if num <= firstMin:
                firstMin = num
            elif num < secondMin:
                secondMin = num
            elif num > secondMin:
                return True

        return False
