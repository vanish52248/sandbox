n, x = map(int, input().split())
c = n
min_ = float('inf')

for _ in range(n):
    m = int(input())
    x -= m
    min_ = min(min_, m)
    
while True:
    if x < min_:
        break
    x -= min_
    c += 1

print(c)