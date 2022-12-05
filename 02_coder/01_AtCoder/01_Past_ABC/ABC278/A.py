n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(k):
    del a[0]
    a.append(0)
    
print(*a)
