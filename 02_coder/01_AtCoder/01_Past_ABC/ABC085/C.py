n, y = map(int, input().split())

ares, bres, cres = -1, -1, -1

for a in range(n+1):
    for b in range(n+1):
        c = n - a - b
        if c < 0 or c > n:
            continue
        
        if 10000 * a + 5000 * b + 1000 * c == y:
            ares, bres, cres = a, b, c
            
print(ares, bres, cres)
