class ConcluSolution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        charDict = {}

        front = 0
        end = 0

        while front <= end and end < n:
            if not s[front] 

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ABDict = {}
        result = 0

        n = len(A)
        for i in range(n):
            for j in range(n):
                currSum = A[i] + B[j]
                if currSum in ABDict:
                    ABDict[currSum] += 1
                else:
                    ABDict[currSum] = 1

        for i in range(n):
            for j in range(n):
                currSum = -(C[i] + D[j])
                if currSum in ABDict:
                    result += ABDict[currSum]

        return result
