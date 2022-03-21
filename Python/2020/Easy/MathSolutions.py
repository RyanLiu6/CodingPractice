from math import sqrt


class MathSolutions:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        retArr = []

        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                retArr.append("FizzBuzz")
            elif i % 5 == 0:
                retArr.append("Buzz")
            elif i % 3 == 0:
                retArr.append("Fizz")
            else:
                retArr.append(i)

        return retArr

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Using Sieve of Eratostheness
        if n < 2:
            return 0

        primeList = [True for _ in range(n)]
        primeList[0] = False
        primeList[1] = False

        for i in range(int(sqrt(n)) + 1):
            if primeList[i]:
                for j in range(i*i, n, i):
                    primeList[j] = False

        return sum(primeList)

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        while n != 1:
            first = n / 3
            second = n // 3
            if first != second:
                return False
            n //= 3

        return True

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        :input: IV
        :output: 4
        """
        roman = self.setUpRoman()
        prev = 1 << 31
        total = 0

        for c in s:
            curr = roman[c]
            print("Prev = " + str(prev))
            print("Curr = " + str(curr))

            if curr > prev:
                total += curr - 2*prev
            else:
                total += curr

            prev = curr
            print("Total = " + str(total), end="\n\n")
        return total

    def setUpRoman(self):
        conv = {}
        conv["I"] = 1
        conv["V"] = 5
        conv["X"] = 10
        conv["L"] = 50
        conv["C"] = 100
        conv["D"] = 500
        conv["M"] = 1000
        return conv
