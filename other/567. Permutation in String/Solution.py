class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ctr = 0
        m = Counter(list(s1))
        for i in range(len(s2)-len(s1)+1):
            stemp = Counter(list(s2[i:i+len(s1)]))
            if (m == stemp):
                return True         
        return False