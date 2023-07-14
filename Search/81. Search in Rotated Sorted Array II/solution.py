class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums = list(set(nums))
        nums.sort()
        l = 0
        r = len(nums)-1
        while(l<=r):
            mid = int(math.floor((l+r)/2))
            if (nums[mid] < target):
                l = mid + 1
            elif (nums[mid] > target):
                r = mid - 1
            else:
                return True
        return False