class IntroSolution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rightSum = leftSum = 0

        for num in nums:
            rightSum += num

        for i in range(len(nums)):
            rightSum -= nums[i]

            if leftSum == rightSum:
                return i

            leftSum += nums[i]

        return -1

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        numDict = {}
        maxNum = -1 << 31
        maxIndex = -1
        isDom = True

        for i in range(n):
            if nums[i] > maxNum:
                maxNum = nums[i]
                maxIndex = i

            numDict[i] = 2 * nums[i]

        for i in range(n):
            if i == maxIndex:
                continue
            if maxNum < numDict[i]:
                return -1

        return maxIndex

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        retStr = ""
        carry = 0

        n = len(a) - 1
        m = len(b) - 1

        while n >= 0 and m >= 0:
            curr = int(a[n]) + int(b[m])
            carry += curr
            retStr += str(carry % 2)
            carry //= 2
            n -= 1
            m -= 1

        for i in range(n, -1, -1):
            print(a[i])
            curr = int(a[i])
            carry += curr
            retStr += str(carry % 2)
            carry //=2

        for i in range(m, -1, -1):
            curr = int(b[i])
            carry += curr
            retStr += str(carry % 2)
            carry //= 2

        if carry == 1:
            retStr += str(1)

        return retStr[::-1]
