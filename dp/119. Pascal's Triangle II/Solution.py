class Solution:
    def getRow(self, rowIndex):
        dp = [[] for _ in range(rowIndex + 1)]
        dp[0].append(1)
        for i in range(1, rowIndex + 1):
            dp[i].append(1)
            for j in range(1, len(dp[i - 1])):
                sum_val = dp[i - 1][j] + dp[i - 1][j - 1]
                dp[i].append(sum_val)
            dp[i].append(1)
        
        return dp[rowIndex]