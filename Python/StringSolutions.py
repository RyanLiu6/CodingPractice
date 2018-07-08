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
        return 0

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
        return False
