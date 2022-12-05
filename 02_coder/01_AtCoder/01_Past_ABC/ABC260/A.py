s = sorted(list(input()))

if s[0] != s[1] != s[2]:
    print(s[0])
elif s[0] == s[1] == s[2]:
    print(-1)
elif s[0] == s[1]:
    print(s[2])
elif s[1] == s[2]:
    print(s[0])
elif s[2] == s[0]:
    print(s[1])