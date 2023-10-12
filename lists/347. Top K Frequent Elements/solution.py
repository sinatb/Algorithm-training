class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        tmp = defaultdict(int)
        for i in nums:
            tmp[i]+=1
        s_tmp = sorted(tmp.items(),key = lambda x : x[1])
        return [s_tmp[len(s_tmp)-1-i][0] for i in range(k)]