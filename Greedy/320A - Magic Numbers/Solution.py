s = input()
i = 0
while i < len(s):
    if s[i:i + 3] == "144":
        i += 3
    elif s[i:i + 2] == "14":
        i += 2
    elif s[i:i + 1] == "1":
        i += 1
    else:
        break
if i < len(s) or i > len(s):
    print("NO")
else:
    print("YES")
