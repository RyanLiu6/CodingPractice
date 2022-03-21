import math


class OtherSolutions:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if not self.isOperator(token):
                stack.append(int(token))
            else:
                # If current token is an operator:
                # Calculate result and add to stack
                second = stack.pop()
                first = stack.pop()
                res = self.calcResult(token, first, second)
                stack.append(res)

        # At the end, there should only be one thing remaining
        return stack[0]

    def isOperator(self, token):
        op = ["+", "-", "*", "/"]
        if token in op:
            return True
        else:
            return False

    def calcResult(self, token, first, second):
        if token == "+":
            return first + second
        elif token == "-":
            return first - second
        elif token == "*":
            return first * second
        elif token == "/":
            return math.trunc(first / second)

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using sort
        # nums.sort()
        # return nums[len(nums) // 2]

        # Find your own
        major = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                major = nums[i]
                count = 1
            elif nums[i] == major:
                count += 1
            else:
                count -= 1

        return major

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        result = 0
        if not tasks:
            return result

        taskDict = {}
        for task in tasks:
            if task in taskDict:
                taskDict[task] += 1
            else:
                taskDict[task] = 1

        current = tasks[0]
        result += 1

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        retStr = "";
        retStr += M[num // 1000]
        retStr += C[(num % 1000) // 100]
        retStr += X[(num % 100) // 10]
        retStr += I[num % 10]

        return retStr

    # def divide(self, dividend, divisor):
    #     """
    #     :type dividend: int
    #     :type divisor: int
    #     :rtype: int
    #     """
    #

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
