a = sorted(list(map(int, input().split())))

flg = False
if (a[0] == a[1] == a[2]):
    if a[3] == a[4]:
        flg = True   
elif (a[2] == a[3] == a[4]):
    if a[0] == a[1]:
        flg = True

print("Yes" if flg else "No")
