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

        n = len(s)

        base = ord("A") - 1

        for i in range(n):
            shift = ord(s[i]) - base
            retInt += shift*(26**(n - i - 1))

        return retInt

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x*x, n / 2)
        else:
            return x*self.myPow(x*x, n // 2)

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        curr = x
        while curr * curr > x:
            curr = (curr + x / curr) // 2
        return int(curr)

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        topChanged = False

        if dividend > 0:
            top = dividend
        else:
            topChanged = True
            top = -dividend

        if divisor > 0:
            bot = divisor
        else:
            bot = -divisor

        while top >= bot:
            top -= bot
            result += 1

        print("Result: ", str(result))
        print("Top: ", str(top))
        print("Bot: ", str(bot))

        if topChanged and bot != divisor:
            # both were different and thus two negatives
            return result
        elif topChanged and bot == divisor:
            return -result
        elif not topChanged and bot != divisor:
            return -result
        else:
            return result

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
