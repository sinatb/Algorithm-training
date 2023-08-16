class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        ans = 999999
        s = 0
        while r != len(nums):
            if s < target:
                s += nums[r]
                r += 1
            while s >= target:
                s -= nums[l]
                l += 1
                if r-l+1 < ans:
                    ans = r-l+1
        if ans == 999999:
            return 0
        return ans