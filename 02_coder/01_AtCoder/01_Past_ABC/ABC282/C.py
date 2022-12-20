n = int(input())
s = list(input())

flg = True
ans = ""
count = 0
for i in range(n):
    if s[i] == '"':
        count += 1
        if count % 2 == 0:
            flg = True
        else:
            flg = False
        ans += '"'
    elif s[i] == ",":
        if flg:
            ans += "."
        else:
            ans += ","
    else:
        ans += s[i]

print(ans)
