class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l = 0
        r = len(s)-1
        while l<r:
            while l < r and not s[l].isalnum(): 
                l += 1
            while r > l and not s[r].isalnum(): 
                r -= 1
            if (s[l].isalnum() and s[r].isalnum() and s[l] != s[r]):
                return False
            l+=1
            r-=1
        return True