class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        self.prepNum()
        return self.numToWords(num)

    def numToWords(self, num):
        retStr = ""
        if num < 10:
            retStr = self.belowTen[num]
        elif num < 20:
            retStr = self.belowTwenty[num - 10]
        elif num < 100:
            retStr = self.belowHundred[num // 10] + " " + self.numToWords(num % 10)
        elif num < 1000:
            retStr = self.numToWords(num // 100) + " Hundred " + self.numToWords(num % 100)
        elif num < 1000000:
            retStr = self.numToWords(num // 1000) + " Thousand " + self.numToWords(num % 1000)
        elif num < 1000000000:
            retStr = self.numToWords(num // 1000000) + " Million " + self.numToWords(num % 1000000)
        else:
            retStr = self.numToWords(num // 1000000000) + " Billion " + self.numToWords(num % 1000000000)

        return retStr.strip()

    def prepNum(self):
        self.belowTen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.belowTwenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.belowHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        num / denom
        """
        if not numerator:
            return "0"

        retStr = ""

        # "+" or "-"
        if (numerator < 0)!= (denominator < 0):
            retStr += "-"

        top = abs(numerator)
        bot = abs(denominator)

        # Integer part
        retStr += str(top // bot)
        top %= bot
        if top == 0:
            return retStr

        # Fractions
        numDict = {}
        retStr += "."

        numDict[top] = len(retStr)

        while top != 0:
            top *= 10
            retStr += str(top // bot)
            top %= bot

            if top in numDict:
                index = numDict[top]
                retStr = retStr[:index] + "(" + retStr[index:] + ")"
                break;
            else:
                numDict[top] = len(retStr)

        return retStr
