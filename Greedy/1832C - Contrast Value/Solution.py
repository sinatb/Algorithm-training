from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    nums = map(int, input().split())
    nums = [i[0] for i in groupby(nums)]
    ans = len(nums)
    i = 0
    while i + 2 < len(nums):
        if nums[i] < nums[i + 1] < nums[i + 2]:
            ans -= 1
        if nums[i] > nums[i + 1] > nums[i + 2]:
            ans -= 1
        i += 1
    print(ans)
