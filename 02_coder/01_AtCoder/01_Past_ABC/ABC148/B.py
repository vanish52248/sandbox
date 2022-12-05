n = input()
s, t = input().split()
r = ""

for i in range(len(s)):
    r += s[i] + t[i]

print(r)