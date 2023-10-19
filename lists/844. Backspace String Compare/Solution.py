class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def delBackspace(st):
            s_str = list(st)
            i=0
            while i != len(s_str) and len(s_str)>0:
                if (s_str[i] == '#'):
                    del s_str[i]
                    if (i>=1):
                        del s_str[i-1]
                    if i>2:
                        i -= 2
                    else:
                        i = 0
                else:
                    i+=1
            return s_str
        s_str = delBackspace(s)
        t_str = delBackspace(t)
        return s_str == t_str