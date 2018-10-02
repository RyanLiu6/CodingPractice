class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Buy and then sell
        if not prices:
            return 0

        buy = prices[0]
        profit = 0

        for p in prices:
            buy = min(buy, p)
            curr = p - buy
            profit = max(profit, curr)

        return profit

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Recursive
        self.DP = [-1 for _ in range(len(s) + 1)]

        return self.decodeHelper(s, len(s))

        # Iterative
        n = len(s)
        if n == 0:
            return 0

        self.DP = [-1 for _ in range(len(s) + 1)]
        self.DP[n] = 1
        self.DP[n - 1] = 0
        if s[0] != "0":
            self.DP[n - 1] = 1

        for i in range(n - 2, -1, -1):
            twoDigit = int(s[i:i + 2])
            oneDigit = int(s[i:i + 1])

            if oneDigit >= 1 and oneDigit <= 9:
                self.DP[i] += self.DP[i + 1]
            if twoDigit >= 10 and twoDigit <= 26:
                self.DP[i] += self.DP[i + 2]

        return self.DP[0]

    def decodeHelper(self, string, k):
        if k == 0:
            return 1

        start = len(string) - k
        if string[start] == "0":
            return 0

        if self.DP[k] != -1:
            return self.DP[k]

        retInt = self.decodeHelper(string, k - 1)
        if k >= 2 and int(string[start:start + 2]) <= 26:
            retInt += self.decodeHelper(string, k - 2)

        self.DP[k] = retInt
        return retInt

    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
