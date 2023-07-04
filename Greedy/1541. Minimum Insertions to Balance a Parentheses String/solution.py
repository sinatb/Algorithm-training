class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        lstack = []
        ctr = 0
        for char in s:
            if (char == '('):
                if (ctr == 1):
                    if (len(lstack)>0):
                        lstack.pop()
                        ret += 1
                    else :
                        ret += 2
                lstack.append(char)
                ctr = 0
            elif (char == ')'):
                ctr += 1
                if (ctr == 2):
                    ctr = 0
                    if len(lstack) > 0:
                        lstack.pop()
                    else:
                        ret += 1
        if (ctr == 1 and len(lstack) == 0):
            ret += 2
        else:
            ret += 2*len(lstack) -ctr
        return ret