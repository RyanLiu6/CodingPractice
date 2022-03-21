from itertools import permutations


class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        maxGap = 0
        currGap = 0
        firstOne = False

        binString = "{0:b}".format(N)

        for bin in binString:
            if bin == "0" and firstOne:
                currGap += 1
            else:
                if not firstOne:
                    firstOne = True
                else:
                    maxGap = max(maxGap, currGap + 1)
                    currGap = 0

        return maxGap

    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N == 1:
            return True

        return self.permuteNum("", str(N))

    def permuteNum(self, prefix, str):
        n = len(str)
        if n == 0:
            return self.checkPowerOf(int(prefix))
        else:
            for i in range(n):
                self.permuteNum(prefix + str[i], str[0:i] + str[i+1:n])

    def checkPowerOf(self, a):
        return (a and (not(a & (a - 1))))
