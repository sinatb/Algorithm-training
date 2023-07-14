class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        hs = set()
        minHeap = []
        heappush(minHeap,(nums1[0]+nums2[0],0,0))
        hs.add((0,0))
        while k > 0 and minHeap:
            s,i,j = heappop(minHeap)
            ans.append([nums1[i],nums2[j]])
            if i < len(nums1)-1 and (i+1,j) not in hs :
                heappush(minHeap,(nums1[i+1]+nums2[j],i+1,j))
                hs.add((i+1,j))
            if j < len(nums2)-1 and (i,j+1) not in hs:
                heappush(minHeap,(nums1[i]+nums2[j+1],i,j+1))
                hs.add((i,j+1))
            k-=1
        return ans          
