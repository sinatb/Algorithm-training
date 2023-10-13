class Solution(object):
    def maxFrequency(self, nums, k):
        maxFreq = 0
        nums.sort()
        i,j = 0,0
        currSum = 0
        while j < len(nums):
            currSum += nums[j]
            while nums[j] * (j - i + 1) > currSum + k: 
                currSum -= nums[i]
                i += 1
            maxFreq = max(maxFreq, j - i + 1)
            j += 1
        return maxFreq