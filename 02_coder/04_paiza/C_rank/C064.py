import math

m, n = map(int, input().split())

c = [int(input()) for _ in range(m)]

a = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(a)):
    total = 0
    for j in range(len(a[0])):
        if a[i][j] == 0:
            continue
        else:
            temp = c[j] / 100
            total += math.floor(temp * a[i][j])
    print(total)
zl
