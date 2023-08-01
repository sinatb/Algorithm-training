class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(nums,ans,k,ret):
            if len(ans) == k:
                ret.append(ans)
            else:
                for i in nums:
                    tmpn = [x for x in nums if x>i]
                    tmpa = ans[:]
                    tmpa.append(i)
                    backtrack(tmpn,tmpa,k,ret)
            return ret
        return backtrack([i for i in range(1,n+1)],[],k,[])