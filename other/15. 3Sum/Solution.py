class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            temp = nums[:]
            target = -temp[i]
            del[temp[i]]
            start = 0
            end = len(temp)-1
            while (start < end):
                if (temp[start] + temp[end] == target):
                    ans.append([temp[start],temp[end],-target])
                    end -= 1
                    start += 1
                elif (temp[start] + temp[end] > target):
                    end-=1
                else:
                    start+=1
        return {tuple(sorted(i)): i for i in ans}.values()
