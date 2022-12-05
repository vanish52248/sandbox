n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
r = 0

for i in range(n):
    if i < k:
        r += l[i]
        
print(r)
    