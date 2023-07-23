class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [False for i in range(len(nums))]
        dp[0] = True
        for i in range(len(nums)-1):
            if (dp[i] == True):
                if (nums[i] > len(nums)):
                    return True
                else:
                    for j in range(nums[i]+1):
                        if (i+j < len(nums)):
                            dp[i+j] = True
                        elif (i+j == len(nums)-1):
                            return True
        return dp[len(nums)-1]