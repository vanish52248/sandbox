n, p = map(int, input().split())
a = list(map(int,input().split()))
c = 0

for i in a:
    if p > i:
        c += 1
        
print(c)
        