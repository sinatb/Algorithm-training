class Solution(object):
    
    def rights_calc(self,rights,nums,i):
        if (i == len(nums)-1):
            return 1
        rights[i] = nums[i+1] * self.rights_calc(rights,nums,i+1)
        return rights[i]
    
    def lefts_calc(self,lefts,nums,i):
        if (i == 0):
            return 1
        lefts[i] = nums[i-1] * self.lefts_calc(lefts,nums,i-1)
        return lefts[i]
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        rights = [1]*len(nums)
        lefts = [1]*len(nums)
        self.rights_calc(rights,nums,0)
        self.lefts_calc(lefts,nums,len(nums)-1)
        for i in range(len(nums)):
            ans.append(lefts[i]*rights[i])
        return ans