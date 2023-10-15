class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans_dict = defaultdict(list)
        for i in range(len(nums)):
            ans_dict[nums[i]].append(i)
        print(ans_dict)
        nums.sort()
        l = 0
        r = len(nums)-1
        while r>l :
            if nums[l] + nums[r] > target:
                r-=1
            elif nums[l] + nums[r] < target:
                l+=1
            else:
                if (nums[l] == nums[r]):
                    return [ans_dict[nums[l]][0],ans_dict[nums[l]][1]]
                return [ans_dict[nums[l]][0],ans_dict[nums[r]][0]] 