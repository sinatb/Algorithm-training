class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(chars,ans,k,answers):
            if (k == len(nums)):
                answers.append(ans)
            else:
                for i in chars:
                    ah = ans[:]
                    ch = chars[:]
                    ch.remove(i)
                    ah.append(i)
                    backtrack(ch,ah,k+1,answers)
            return answers
        return backtrack(nums,[],0,[])