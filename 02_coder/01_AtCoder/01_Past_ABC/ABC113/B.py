n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

ans = 1000
result = 0
for i, v in enumerate(h, start=1):
    temp = t - v * 0.006
    if ans > abs(a-temp):
        result = i
        ans = abs(a-temp)
print(result)
