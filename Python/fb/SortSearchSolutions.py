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

        for price in prices:
            buy = min(buy, price)
            currP = price - buy
            profit = max(profit, currP)

        return profit
