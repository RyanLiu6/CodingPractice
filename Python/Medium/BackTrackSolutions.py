class BackSolutions:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        retArr = []
        if not digits:
            return retArr

        self.prepNumbers()
        retArr.append("")

        for digit in digits:
            num = int(digit)
            curr = self.numDict[num]

            temp = []

            for i in range(len(curr)):
                for j in range(len(retArr)):
                    temp.append(retArr[j] + curr[i])

            retArr = temp

        return retArr

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

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retArr = []
        if not nums:
            return retArr


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retArr = []
        if not nums:
            return retArr

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
