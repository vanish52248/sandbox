n, l = map(int, input().split())

apples = [0] * n
ans = 0

for i in range(n):
    apples[i] = l + i

current = 0
min_ = 1000
for i in range(n):
    current = sum(apples)-apples[i]
    if abs(sum(apples)-current) < min_:
        min_ = abs(sum(apples)-current)
        ans = current
print(ans)
        