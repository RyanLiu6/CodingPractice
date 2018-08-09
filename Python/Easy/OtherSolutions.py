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
