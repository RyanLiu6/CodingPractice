class OtherSolutions:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        while n != 0:
            count = count + (n & 1)
            n = n >> 1

        return count

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0

        while x != 0 and y != 0:
            first = x & 1
            second = y & 1
            if first != second:
                count += 1

            x = x >> 1
            y = y >> 1

        while x != 0:
            count = count + (x & 1)
            x = x >> 1

        while y != 0:
            count = count + (y & 1)
            y = y >> 1

        return count

    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 32 bits
        m = 32
        retInt = 0
        tempArr = []
        for i in range(m):
            tempArr.append(n & 1)
            n = n >> 1

        for i in range(m - 1, -1, -1):
            retInt += tempArr[i]*(2**(m - i - 1))

        return retInt

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        Input: "()[]{}"
        Output: true

        Input: "([)]"
        Output: false

        Input: "{[]}"
        Output: true
        """
        if not s:
            return True

        if len(s) % 2:
            return False

        left = self.prepLeft()
        right = self.prepRight()
        pStack = []

        for c in s:
            if c in left:
                pStack.append(c)
            if c in right:
                head = pStack.pop()
                if right[c] != head:
                    return False

        return True

    def prepLeft(self):
        dict = {}
        dict["("] = ")"
        dict["{"] = "}"
        dict["["] = "]"

        return dict

    def prepRight(self):
        dict = {}
        dict[")"] = "("
        dict["}"] = "{"
        dict["]"] = "["

        return dict

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        actual = 0
        n = len(nums)
        for num in nums:
            actual += num

        expected = (n)*(n + 1) / 2
        return int(expected - actual)
