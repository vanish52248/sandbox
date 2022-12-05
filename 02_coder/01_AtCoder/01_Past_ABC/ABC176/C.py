n = int(input())
a = list(map(int, input().split()))
current = a[0]
c = 0

for i in range(1, n):
    if current > a[i]:
        c += abs(current-a[i])    
        current = max(current, a[i])
    elif current <= a[i]:
        current = max(current, a[i])
print(c)