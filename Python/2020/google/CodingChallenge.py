import math
import collections

class CCSolutions:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # Math Solution
        minAmount = math.ceil(len(B) / len(A))

        for i in range(2):
            if B in (A)*(minAmount + i):
                return minAmount + i

        return -1

    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
              flowers[i] = x -> flower x blooms on day i
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        flowerBed = {}

        for day in range(n):
            bloom = flowers[day]

        return -1

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        :input: S = "2-5g-3-J", K = 2
        :output: "2-5G-3J"
        """
        count = 0
        retStr = ""
        baseStr = S.upper().replace("-", "")

        for i in range(len(baseStr) - 1, -1, -1):
            retStr += baseStr[i]
            count += 1

            if count == K and i != 0:
                retStr += "-"
                count = 0

        return retStr[::-1]

    def canJumpToRoot(self, D, A):
        """
        :type nums: List[int]
        :type D: int
        :rtype: List[int]
        :input: nums = [-1, 0, 1, 2, 3], D = 2
        :output: [-1, -1, 0, 1, 2]
        """
        n = len(A)
        retArr = [-1 for _ in range(n)]

        if not A:
            return retArr

        for i in range(n):
            retArr[i] = self.helper(A, D, i)

        return retArr

    def helper(self, A, D, index):
        if D == 0:
            return index

        if A[index] == -1:
            return -1

        return self.helper(A, D - 1, A[index])
