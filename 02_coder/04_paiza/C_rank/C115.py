n, m = map(int, input().split())
result = 0

for _ in range(n-1):
    a = int(input())
    if m >= a:
        result += a
        
print(result)
