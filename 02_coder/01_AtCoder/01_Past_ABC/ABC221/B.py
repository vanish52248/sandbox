s = list(input())
t = list(input())
i = 1
if s == t:
        print("Yes")
        exit()
else:
    for i in range(len(s)-1):
        s[i], s[i+1] = s[i+1], s[i]
        if s == t:
            print("Yes")
            exit()
        s[i], s[i+1] = s[i+1], s[i]
print("No")