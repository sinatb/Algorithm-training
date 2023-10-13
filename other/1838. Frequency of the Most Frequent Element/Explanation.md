# The Solution

My first Solution for this problem was to sort the array and try to get the maximum length from adding part of `k` to the elements smaller than the biggest element.

```python
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        ans = 0
        for i in range(len(nums)-1,-1,-1):
            tmp_ans = 0
            tmp_k = k
            for j in range(i,-1,-1):
                if (nums[j]==nums[i]):
                    tmp_ans+=1
                else:
                    tmp_k -= nums[i]-nums[j]
                    if (tmp_k>=0):
                        tmp_ans+=1
                    else:
                        break
            if (tmp_ans > ans):
                ans = tmp_ans
            if (ans > i+1):
                break
        return ans
```

This solution is correct but has a very long execution time.
The second solution is to use a sliding window approach. At first we sort the array and then initialize a window at the starting point of the array. At each step we add the rightmost element to the window. If the sum of all elements in the new window is equal to the maximum element*number of elements the window is valid, Else we need to move the left most element of the window.
The answer is inside one of these valid windows (the one with the maximum length).
