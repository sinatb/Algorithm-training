class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        k = -1
        while start <= end:
            mid = (start + end)//2
            if (nums[mid] > nums[-1]):
                start = mid + 1
            else:
                end = mid - 1
        k = start
        print(k)
        shift = len(nums) - k
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)//2
            print((mid-shift)%len(nums))
            if (nums[(mid-shift)%len(nums)] == target):
                return (mid-shift)%len(nums)
            elif (nums[(mid-shift)%len(nums)] > target):
                end = mid - 1
            else:
                start = mid + 1
        return -1