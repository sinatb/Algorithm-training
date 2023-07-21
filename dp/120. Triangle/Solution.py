class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        m = n+1
        dp = [[float("inf") for i in range(m)] for j in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            for j in range(i+1):
                if (j==0):
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif (j==i):
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j],dp[i-1][j-1])
        return min(dp[n-1])