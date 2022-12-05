n = int(input())
ans = str(hex(n)[2:]).upper()

if len(ans) == 1:
    print("0" + str(ans))
else:
    print(ans)
