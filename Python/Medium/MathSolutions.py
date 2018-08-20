class MathSolutions:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = 0
        numSet = set()
        strNum = str(n)

        while result != 1:
            result = 0
            for num in strNum:
                curr = int(num)*int(num)
                result += curr
            if result in numSet:
                return False
            strNum = str(result)
            numSet.add(result)

        return True

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        Time complexity must be O(logn)
        """
        count = 0
        factor = 5

        while n / factor >= 1:
            count += (n // factor)
            factor *= 5

        return count

        # Recursive
        if n < 5:
            return 0
        return n//5 + self.trailingZeroes(n // 5)

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        retInt = 0
        if not s:
            return retInt

        base = ord("A")

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        answer = 1
        negative = False

        if n == 0:
            return answer
        if n < 0:
            negative = True
            n *= -1

        answer = x
        for i in range(1, n):
            answer *= x

        if negative:
            answer = 1 / answer

        return answer

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        retStr = ""

        if numerator < 0 ^ denominator < 0:
            retStr += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
