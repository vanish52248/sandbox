n, m, t = map(int, input().split())
a = list(map(int, input().split()))

xy = {}
for i in range(m):
    x, y = map(int, input().split())
    xy[x] = y

for i in range(1, n):
    if i in xy.keys():
        t += xy[i]
    t -= a[i-1]
    if t <= 0:
        print("No")
        break
else: 
    print("Yes")
