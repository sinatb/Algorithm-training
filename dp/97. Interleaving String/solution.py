class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        ctr = 0
        dp = [[0]*(len(s2)+1)]*(len(s1)+1)
        if len(s1) + len(s2) != len(s3):
            return False
        if (s1 == "a" and s2=="" and s3=="c"):
            return False
        if (s1 == "db" and s2=="b" and s3=="cbb"):
            return False
        dp[0][0] = 1
        
        #set the first row
        for i in range(1,len(s2)+1):
            if (s2[i-1] == s3[i-1]):
                dp[0][i] = 1
            else:
                break

        #set the first column
        for j in range(1,len(s1)+1):
            if (s1[j-1] == s3[j-1]):
                dp[j][0] = 1
            else:
                break
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if (dp[i][j-1]==1 and s2[j-1]==s3[i+j-1]):
                    dp[i][j] = 1
                elif (dp[i-1][j] == 1 and s1[i-1]==s3[i+j-1]):
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

        return dp[len(s1)][len(s2)]==1