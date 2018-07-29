class TwoPSolution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        retStr = list(s)
        n = len(s)
        i = 0
        j = n - 1

        while i < j:
            retStr[i], retStr[j] = retStr[j], retStr[i]

            i += 1
            j -= 1

        return "".join(retStr)

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()

        return sum(nums[::2])

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i = 0
        j = n - 1

        while i < j:
            curr = numbers[i] + numbers[j]

            if curr == target:
                return [i + 1, j + 1]
            elif curr < target:
                i += 1
            elif curr > target:
                j -= 1

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        n = len(nums)
        if not nums:
            return j

        for i in range(n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: [1,1,0,1,1,1]
        Output: 3
        """
        if not nums:
            return 0

        maxOnes = 0
        currOnes = 0

        for num in nums:
            if num == 1:
                currOnes += 1
            else:
                maxOnes = max(currOnes, maxOnes)
                currOnes = 0

        maxOnes = max(maxOnes, currOnes)
        return maxOnes

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        minSize = n + 1
        front = end = cSum = 0

        while end < n:
            cSum += nums[end]
            end += 1

            print(front, end, end=" |")
            print(cSum)

            while cSum >= s:
                minSize = min(minSize, end - front)
                cSum -= nums[front]
                front += 1

        if minSize == n + 1:
            return 0
        else:
            return minSize
