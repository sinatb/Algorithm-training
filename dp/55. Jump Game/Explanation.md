# The Solution

So my Solution is pretty self Explanatory,it starts from the far left side of the list and calculates all the reachable points from each starting index.If a point is reachable it puts True in the dp table for that index.If the last index has True in the dp table we can say that we have an answer.This solution however is very slow.The alternative Solution is :

```python
 class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums)-1
        
        for i in range(len(nums)-2,-1,-1): # Iterate backwards from second to last item until the first item
            if (i + nums[i]) >= last_position: # If this index has jump count which can reach to or beyond the last position
                last_position = i # Since we just need to reach to this new index
        return last_position == 0
```

In The alternate Solution, The `last_position` determines the last point that we can reach the last index from it.If this point is 0 then we can say the problem has a solution.At each iteration of the for loop we go back further in the nums array and determine the new last position.This determination is done if we know we can reach the current last position from the current point in array.
  