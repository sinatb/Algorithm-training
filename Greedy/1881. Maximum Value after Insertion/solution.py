class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        is_negative = n[0] == '-'
        p = len(n)
        for i in range(len(n)):
            if (not is_negative):
                if (x > int(n[i])):
                    p = i
                    break
            else:
                if (i>0 and x < int(n[i])):
                    p = i
                    break
        output = n[:p] + str(x) + n[p:]
        return output