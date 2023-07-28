class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctr = defaultdict(int)
        lo = 0
        ans = 0
        for i in range(len(s)):
            ctr[s[i]] += 1
            while max(ctr.values()) > 1:
                ctr[s[lo]] -= 1
                lo += 1
            ans = max(ans,i-lo+1)
        return ans