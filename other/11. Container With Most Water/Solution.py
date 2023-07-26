class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        ma = -1
        while start < end:
            curr = (end-start) * min(height[start],height[end])
            ma = max(curr,ma)
            if (height[start] > height[end]):
                end -= 1
            else:
                start += 1
        return ma