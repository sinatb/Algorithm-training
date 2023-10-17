class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_dict = defaultdict(str)
        for i in range(len(s)):
            if(not t_dict[s[i]]):
                if (t[i] in t_dict.values()):
                    return False
                t_dict[s[i]] = t[i]
            else:
                if (t_dict[s[i]] != t[i]):
                    return False
        return True
        