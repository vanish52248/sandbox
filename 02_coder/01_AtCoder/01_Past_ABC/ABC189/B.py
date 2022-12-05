n, x = map(int, input().split())
alchol = 0

for i in range(1, n+1):
    v, p = map(int, input().split())
    alchol += (v * p)
    if alchol > x * 100:
        print(i)
        exit()
print(-1)