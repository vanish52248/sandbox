s = list(map(str, input().split()))
t = list(map(str, input().split()))

if s == t:
    print("Yes")
else:
    if s[0] == t[0] and s[1] == t[2]:
        print("No")
    else:
        print("Yes")
   