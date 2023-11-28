for _ in range(int(input())):
    num = int(input())
    root = int(round(num ** (1./3)))
    if root ** 3 == num:
        print("NO")
    else:
        start = 0
        end = root
        tf = False
        while start <= end:
            ans = start ** 3 + end**3
            if ans == num:
                tf = True
                break
            elif ans > num:
                end -= 1
            else:
                start += 1
        if tf:
            print("YES")
        else:
            print("NO")
