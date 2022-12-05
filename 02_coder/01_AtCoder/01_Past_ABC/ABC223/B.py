s = input()
t = []

for i in range(len(s)):
    t.append(s[i:]+s[:i])

t.sort()

print(t[0])
print(t[-1])