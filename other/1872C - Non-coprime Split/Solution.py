def solve(l, r):
    for i in range(l, r + 1):
        for j in range(2, round(i ** 0.5) + 1):
            if i % j == 0:
                print(j, i - j)
                return
    print(-1)
    return


t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    solve(l, r)
