s = list(input())

flg = True
for i in range(1, len(s)+1):
    if i % 2 == 0:
        if s[i-1] != "L" and s[i-1] != "U" and s[i-1] != "D":
            flg = False
            break
    else:
        if s[i-1] != "R" and s[i-1] != "U" and s[i-1] != "D":
            flg = False
            break
print("Yes" if flg else "No")