class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
   
        for i in range(1,m):
            for j in range(1,n):
                lc = 0
                uc = 0
                if obstacleGrid[i-1][j]!=1:
                    uc = dp[i-1][j]
                if obstacleGrid[i][j-1]!=1:
                    lc = dp[i][j-1]
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = lc+uc
        print(dp)
        return dp[m-1][n-1]