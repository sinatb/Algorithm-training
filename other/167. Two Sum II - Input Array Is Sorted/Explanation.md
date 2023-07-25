# The Solution

So at first my idea for solving this problem was the most obvious solution.

```python
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
```

As You would expect This solution gets time limit exceeded error.The Second Solution however uses the fact that the array is sorted.We can place a pointer at each side of the array and then move them by comparing their sum with the target.This solution has a linear time order.
