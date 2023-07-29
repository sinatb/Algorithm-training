class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        maxp = 0

        while r!=len(prices):
            profit = prices[r] - prices[l]
            maxp = max(maxp,profit)
            if profit < 0:
                l = r
            r += 1
        return maxp