class ArraySolutions:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :input: [1,1,2]
        :output: 2 w/ [1,2,whatever]
        """
        if not nums:
            return 0

        tail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[tail]:
                tail+=1
                nums[tail] = nums[i]

        return tail + 1

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :input: [7,1,5,3,6,4]
        :output: 7
        """
        if not prices:
            return 0

        buy = prices[0]
        profit = 0

        for price in prices:
            if price < buy:
                buy = price
            else:
                profit+=price-buy
                buy = price

        return profit

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or k == 0:
            return

        n = len(nums)

        for i in range(self.gcd(n,k)):
            currComplete = False
            currIndex = i
            temp = nums[currIndex]
            swap = 0

            while not currComplete:
                newIndex = (currIndex + k) % n
                swap = nums[newIndex]
                nums[newIndex] = temp
                temp = swap
                currIndex = (currIndex + k) % n

                if currIndex == i:
                    currComplete = True

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # O(n) time and space
        dupDict = {}
        for i in range(len(nums)):
            if dupDict.get(nums[i],-1) is -1:
                dupDict[nums[i]] = 1
            else:
                return True

        return False

        # O(n) time and O(1) space if numbers are between 0 and n-1
        for i in range(len(nums)):
            if nums[abs(nums[i])] >= 0:
                nums[abs(nums[i])]*=-1
            else:
                return True

        return False

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time and space
        numDict = {}
        retVal = -1
        for i in range(len(nums)):
            if dupDict.get(nums[i],-1) is -1:
                numDict[nums[i]] = 1
            else:
                numDict[nums[i]]+=1

        for key, value in numDict.items():
            if value is 1:
                retVal = key

        return retVal

        # O(n) time and space
        # numSet = set():
        # for num in nums:
        #     if num in numSet:
        #         numSet.remove(num)
        #     else:
        #         numSet.add(num)
        #
        # return numSet.pop()

        # O(n) time and O(1) space
        retVal = 0
        for num in nums:
            retVal^=num

        return retVal

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 is 0 or n2 is 0:
            return []

        if n1 is 0 and n2 is not 0:
            return nums2

        if n1 is not 0 and n2 is 0:
            return nums1

        if n1 < n2:
            return self.intHelper(nums1, nums2)
        else:
            return self.intHelper(nums2, nums1)

    def intHelper(self, a, b):
        # Assume that len(a) < len(b)
        numDict = {}
        retArr = []

        for num in a:
            if numDict.get(num, -1) is -1:
                numDict[num] = 1
            else:
                numDict[num]+=1

        for num in b:
            currVal = numDict.get(num, -1)
            if currVal is not -1 and currVal > 0:
                retArr.append(num)
                numDict[num]-=1

        return retArr

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        carry = 1

        for i in range(n - 1, -1, -1):
            currVal = digits[i] + carry
            carry = currVal // 10

            digits[i] = currVal % 10

        if carry:
            digits.insert(0, 1)

        return digits

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        :input: [0,1,0,3,12]
        :output: [1,3,12,0,0]
        """
        n = len(nums)
        if not nums:
            return

        # # O(n^2) time
        # for i in range(n):
        #     if nums[i] is 0:
        #         nums.append(0)
        #         nums.remove(0)
        #         i+=1

        # O(n) time
        zero = 0
        for i in range(n):
            if nums[i] is not 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero+=1

        for num in nums:
            print(num)

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}

        for i in range(len(nums)):
            numDict[nums[i]] = i

        for i in range(len(nums)):
            currTarget = target - nums[i]
            val = numDict.get(currTarget, -1)
            if val is not -1 and numDict[currTarget] is not i:
                return (i, numDict[currTarget])

        return (0,0)

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Rows
        n = len(board)

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        :input:     [4,8]
                    [3,6]

        :output:    [3,4]
                    [6,8]
        """
        n = len(matrix)
        matrix.reverse()

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
