n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0

ma = max(a)
mb = min(b)

for i in range(ma, mb+1):
    c += 1
    
print(c)