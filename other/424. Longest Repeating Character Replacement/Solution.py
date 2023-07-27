class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        lo = 0
        ans = 1
        ctr = defaultdict(int)
        for i in range(len(s)):
            ctr[s[i]]+=1
            while (i-lo+1-max(ctr.values()) > k):
                ctr[s[lo]] -= 1
                lo+=1
            ans = max(ans,i-lo+1)
            
        return ans