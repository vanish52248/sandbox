n = int(input())

a = list(map(int, input().split()))
max = 0
ans = 0

for i in range(2, 1001):
    count = 0
    for j in range(n):
        if a[j] % i == 0:
            count += 1
    if max < count:
        ans = i
        max = count
print(ans)