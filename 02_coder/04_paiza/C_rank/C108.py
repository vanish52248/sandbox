n = int(input())

x = []
for _ in range(n):
    x.append(int(input()))

c = []
for _ in range(n):
    c.append(list(map(int, input().split())))
    
k = int(input())

total = 0
previous = 1
for i in range(k):
    y = int(input())
    total += x[y-1]
    if 1 <= i < k:
        total += c[previous-1][y-1]
    previous = y
    
print(total)
