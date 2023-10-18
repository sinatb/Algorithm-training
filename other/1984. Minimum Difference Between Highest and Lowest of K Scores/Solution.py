class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = 99999999
        for i in range(len(nums)-k+1):
            if (nums[k+i-1] - nums[i] < ans):
                ans = nums[k+i-1] - nums[i]
        return ans