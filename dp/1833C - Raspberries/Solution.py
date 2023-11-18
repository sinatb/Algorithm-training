for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    evens = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            evens += 1
        nums[i] = k - (nums[i] % k)

    nums.sort()
    if nums[-1] == k:
        print(0)
    else:
        if k != 4:
            print(nums[0])
        else:
            print(min(nums[0], max(0, 2-evens)))
