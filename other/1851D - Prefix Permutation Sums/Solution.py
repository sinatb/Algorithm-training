for _ in range(int(input())):
    n = int(input())
    max_sum = n*(n+1)//2
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        if nums[i] > max_sum:
            print("NO")
            break

