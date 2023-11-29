def argmin(numbers):
    min_num = 9999999999
    arg = -1
    for i in range(len(numbers)):
        if numbers[i] < min_num:
            min_num = numbers[i]
            arg = i
    return arg


for _ in range(int(input())):
    num = int(input())
    ls = list(map(int, input().split()))
    index = argmin(ls)
    is_sorted = all(ls[i] <= ls[i+1] for i in range(index, len(ls) - 1, 1))
    if is_sorted:
        print(index)
    else:
        print(-1)

