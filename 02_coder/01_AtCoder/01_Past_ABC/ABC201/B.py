n = int(input())
m = []

for _ in range(n):
    s, t  = map(str, input().split())
    t = int(t)
    m.append([t, s])

m.sort(reverse=True)

print(m[1][1])