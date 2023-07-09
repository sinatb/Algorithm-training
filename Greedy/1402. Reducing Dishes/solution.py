class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        total = 0
        out = 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1]+total >= 0:
            total += satisfaction.pop()
            out += total
        return out