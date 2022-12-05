n, a, b = map(int, input().split())
m =0

for i in range(1, n+1):
    x = sum(list(map(int, str(i))))
    if a <= x <= b:
        m += i
        
print(m)