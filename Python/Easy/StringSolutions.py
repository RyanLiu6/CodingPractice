class StringSolutions:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negFlag = False
        if x < 0:
            x *= -1
            negFlag = True

        result = 0

        while x > 0:
            curr = x % 10
            result = result * 10 + curr
            x = x // 10

            if result < -1 << 31 or result > (1 << 31) - 1:
                return 0

        if negFlag:
            result*=-1

        return result

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionaries
        uniqDict = {}
        n = len(s)

        for i in range(n):
            val = uniqDict.get(s[i], -1)
            if val is -1:
                uniqDict[s[i]] = (i, 1)
            else:
                currOccur = val[1] + 1
                uniqDict[s[i]] = (i, currOccur)

        for i in range(n):
            val = uniqDict.get(s[i])
            if val[1] == 1:
                return val[0]

        return -1

        # Freq Map
        freq = [0] * 26
        n = len(s)

        for i in range(n):
            freq[ord(s[i]) - 97]+=1

        for i in range(n):
            if freq[ord(s[i]) - 97] == 1:
                return i

        return -1

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        firstLen = len(s)
        secondLen = len(t)

        if firstLen != secondLen:
            return False

        freq = [0] * 26

        for i in range(firstLen):
            freq[ord(s[i]) - 97]+=1

        for i in range(secondLen):
            freq[ord(t[i]) - 97]-=1
            if freq[ord(t[i]) - 97] < 0:
                return False

        return True

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        front = 0
        end = len(s) - 1
        s = s.lower()

        while front <= end:
            # Check for characters
            while front <= end and not s[front].isalnum():
                front+=1

            while front <= end and not s[end].isalnum():
                end-=1

            # Both are charaters now
            if front <= end and s[front] != s[end]:
                return False
            front+=1
            end-=1

        return True

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n = len(str)
        resArr = []
        resNum = 0
        firstNum = False
        negFlag = False

        for i in range(n):
            if str[i].isspace() and not firstNum:
                continue
            if str[i] == "-" and not firstNum:
                negFlag = True
                firstNum = True
                continue
            if str[i] == "+" and not firstNum:
                negFlag = False
                firstNum = True
                continue
            if not str[i].isnumeric() and not firstNum:
                return 0
            if not str[i].isnumeric() and firstNum:
                break

            if str[i].isnumeric():
                # Then we can start interpreting
                firstNum = True
                resArr.append(str[i])

        m = len(resArr)

        for i in range(m):
            resNum = resNum * 10 + int(resArr[i])

        if negFlag:
            resNum*=-1

        if resNum > (1 << 31) - 1:
            return (1 << 31) - 1
        if resNum < (-1 << 31):
            return (-1 << 31)

        return resNum

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        resStr = ""
        prevStr = self.countAndSay(n - 1)
        n = len(prevStr)
        currLet = prevStr[0]
        count = 1

        for i in range(1, n):
            if prevStr[i] == currLet:
                count+=1
            else:
                resStr+=(str(count))
                resStr+=(currLet)
                currLet = prevStr[i]
                count = 1

        # Check if last few nums are same
        if count > 0:
            resStr+=(str(count))
            resStr+=(currLet)

        return resStr

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        :input: ["flower","flow","flight"]
        :output: "fl"
        """
        if not strs:
            return ""

        shortestStr = min(strs, key=len)
        n = len(shortestStr)

        for i in range(n):
            for str in strs:
                if str[i] != shortestStr[i]:
                    return shortestStr[:i]

        return shortest
