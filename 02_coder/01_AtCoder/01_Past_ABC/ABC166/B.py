n, k = map(int, input().split())
lst = []
c = 0

for i in range(k):
    d = int(input())
    a = map(int, input().split())
    for i in a:
        lst.append(i)
        
for i in range(1, n+1):
    if i not in lst:
        c += 1
        
print(c)