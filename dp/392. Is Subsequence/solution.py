class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        print(s)
        print(t)
        dp = [0]
        for i in range(len(t)):
            if (t[i]==s[dp[i]]):
                if (dp[i]+1 == len(s)):
                    return True
                dp.append(dp[i]+1)
            else:
                dp.append(dp[i])
        return False