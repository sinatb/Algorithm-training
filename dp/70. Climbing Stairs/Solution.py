class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0,1,2]
        if n < 3:
            return dp[n]
        else:
            for i in range(3,n+1):
                dp.append(dp[i-1] + dp[i-2])
            return dp[n]