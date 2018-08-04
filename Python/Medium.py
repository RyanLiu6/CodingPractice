class MediumSolution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        self.count = 0
        subStrList = [[-1 for _ in range(n)] for _ in range(n)]

        def subStrHelper():
            for i in range(n):
                for j in range(n):
                    if subStrList[i][j] == -1 and i <= j:
                        if self.isPalindrome(s[i:j+1]):
                            self.count += 1
                        subStrList[i][j] = 1

        subStrHelper()
        return self.count

    def isPalindrome(self, s):
        return s == s[::-1]
