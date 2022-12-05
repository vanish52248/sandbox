x, n = map(int, input().split())
p = list(map(int, input().split()))
temp = float('inf')
ans = 0

for i in range(1000):
    if i not in p:
        if abs(x-i) < temp:
            temp = x-i
            ans = i
print(ans)