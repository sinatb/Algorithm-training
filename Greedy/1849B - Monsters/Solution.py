for _ in range(int(input())):
    n, k = map(int, input().split())
    L = list(map(int, input().split()))
    L = list(map(lambda x: x % k if x % k != 0 else k, L))
    L2 = []
    for i in range(len(L)):
        L2.append((L[i], i))
    L2.sort(key=lambda x: (-x[0], x[1]))
    for i in L2:
        print(i[1]+1)
