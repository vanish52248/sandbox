n = int(input())
d, x = map(int, input().split())
ans = 0

for _ in range(n):
    a = int(input())
    eat = 1
    now = 1
    for _ in range(100):
        now += a
        if now <= d:
            eat += 1
            
    ans += eat
ans = ans + x
print(ans)
            