n = int(input())
s = []
for _ in range(n):
    s_ = int(input())
    s.append(s_)

m = int(input())

for i in range(m):
    a, b, x = map(int, input().split())
    if s[a-1] - x < 0:
        x = x - (abs(x-s[a-1]))
        s[a-1] = 0
    else:
        s[a-1] -= x
    s[b-1] += x

for i in s:
    print(i)
