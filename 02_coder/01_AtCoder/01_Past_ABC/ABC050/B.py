n = int(input())
t = list(map(int, input().split()))
m = int(input())
p = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    current = 0
    for j in range(1,n+1):
        if j == (p[i][0]):
            current += p[i][1]
        else:
            current += t[j-1]
    print(current)