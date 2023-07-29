class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l + r)//2
            if nums[mid]>nums[-1]:
                l = mid + 1
            elif nums[mid]<nums[-1]:
                r = mid 
        return nums[l]