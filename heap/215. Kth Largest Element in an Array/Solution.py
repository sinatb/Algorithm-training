class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        elements = map(lambda x : -x,nums)
        heapq.heapify(elements)
        for _ in range(k-1):
            heapq.heappop(elements)
        return -list(elements)[0]