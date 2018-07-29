class ConcluSolution:
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

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Factorials O(k * k!) tme
        # retList = []
        #
        # for i in range(rowIndex + 1):
        #     retList.append(int(self.choose(rowIndex, i)))
        #
        # return retList

        # Iterative 2
        retList = []

        for i in range(rowIndex + 1):
            retList.append(1)
            for j in range(i - 1, 0, -1):
                retList[j] = retList[j] + retList[j - 1]

        return retList

    def choose(self, n, k):
        top = self.factorial(n)
        bot = self.factorial(k) * self.factorial(n - k)

        return top / bot

    def factorial(self, num):
        if num == 0:
            return 1
        else:
            return num * self.factorial(num - 1)

    def reverseWords_II(self, s):
        """
        :type s: str
        :rtype: str
        """
        retStr = ""
        if not s:
            return retStr

        strList = s.split()

        # return " ".join(strList[::-1])

        for i in range(len(strList) - 1, -1, -1):
            retStr += strList[i]
            if i > 0:
                retStr += " "

        return retStr

    def reverseWords_III(self, s):
        """
        :type s: str
        :rtype: str
        Input: "Let's take LeetCode contest"
        Output: "s'teL ekat edoCteeL tsetnoc"
        """
        retStr = ""
        if not s:
            return retStr

        strList = s.split()
        n = len(strList)

        for i in range(n):
            retStr += strList[i][::-1]
            if i < n - 1:
                retStr += " "

        return retStr

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: [1,1,2]
        Output: 2 w/ [1,2,whatever]
        """
        if not nums:
            return 0

        n = len(nums)
        tail = 0

        for i in range(n - 1):
            if nums[i] != nums[i + 1]:
                nums[tail] = nums[i]
                tail += 1

        nums[tail] = nums[n - 1]
        tail += 1
        return tail

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        n = len(nums)
        tail = 0

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail += 1
