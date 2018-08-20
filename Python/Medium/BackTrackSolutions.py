class BackSolutions:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Using loops
        # self.retArr = []
        # if not digits:
        #     return self.retArr
        #
        # self.prepNumbers()
        # self.retArr.append("")
        #
        # for digit in digits:
        #     num = int(digit)
        #     curr = self.numDict[num]
        #
        #     temp = []
        #
        #     for i in range(len(curr)):
        #         for j in range(len(self.retArr)):
        #             temp.append(self.retArr[j] + curr[i])
        #
        #     self.retArr = temp
        #
        # return self.retArr

        # Backtrack
        retArr = []
        self.prepNumbers()

        self.letterHelper(retArr, digits, "", 0)
        return retArr

    def letterHelper(self, retArr, digits, prefix, index):
        if len(prefix) == len(digits):
            retArr.append(prefix)
            return

        num = self.numDict[int(digits[index])]

        for n in num:
            self.letterHelper(retArr, digits, prefix + n, index + 1)

    def prepNumbers(self):
        dict = {}
        dict[2] = "abc"
        dict[3] = "def"
        dict[4] = "ghi"
        dict[5] = "jkl"
        dict[6] = "mno"
        dict[7] = "pqrs"
        dict[8] = "tuv"
        dict[9] = "wxyz"

        self.numDict = dict

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        retArr = []
        self.pN = n
        self.parenthesisHelper(retArr, "", 0, 0)
        return retArr

    def parenthesisHelper(self, retArr, prefix, open, close):
        if len(prefix) == 2*self.pN:
            retArr.append(prefix)
            return

        # Only have exactly n open parenthesises
        # Only have close parenthesises if there close < open
        if open < self.pN:
            self.parenthesisHelper(retArr, prefix + "(", open + 1, close)
        if close < open:
            self.parenthesisHelper(retArr, prefix + ")", open, close + 1)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retArr = []

        self.permuteHelper(retArr, nums, [])
        return retArr

    def permuteHelper(self, retArr, nums, prefix):
        if len(prefix) == len(nums):
            temp = [p for p in prefix]
            retArr.append(temp)
            return

        for i in range(len(nums)):
            if nums[i] in prefix:
                continue
            prefix.append(nums[i])
            self.permuteHelper(retArr, nums, prefix)
            del(prefix[-1])

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        retArr = []

        self.subsetHelper(retArr, nums, [], 0)
        return retArr

    def subsetHelper(self, retArr, nums, prefix, index):
        retArr.append(prefix)

        for i in range(index, len(nums)):
            self.subsetHelper(retArr, nums, prefix + [nums[i]], i + 1)

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.row = len(board)
        self.col = len(board[0])
        self.size = len(word)
        self.word = word
        self.visited = [[False for x in range(self.col)] for y in range(self.row)]

        for i in range(self.row):
            for j in range(self.col):
                if self.searchHelper(board, 0, i, j):
                    return True

        return False

    def searchHelper(self, board, index, i, j):
        if index == self.size:
            return True

        if 0 <= i < self.row and 0 <= j < self.col and not self.visited[i][j]:
            if board[i][j] == self.word[index]:
                self.visited[i][j] = True
                if self.searchHelper(board, index + 1, i - 1, j):
                    return True
                elif self.searchHelper(board, index + 1, i + 1, j):
                    return True
                elif self.searchHelper(board, index + 1, i, j - 1):
                    return True
                elif self.searchHelper(board, index + 1, i, j + 1):
                    return True
                else:
                    self.visited[i][j] = False
                    return False
        else:
            return False
