n = int(input())
s = []
t = []
c = 1
for i in range(n):
    a, b = input().split()
    s.append(a)
    t.append(b)
 
for i in range(n):
    if s.count(s[i]) > 1 or t.count(s[i]) >= 1:
        if t.count(t[i]) > 1 or s.count(t[i]) >= 1:
            if s[i] != t[i]:
                c = 0
                break
if c == 1:
    print("Yes")
else:
    print("No")