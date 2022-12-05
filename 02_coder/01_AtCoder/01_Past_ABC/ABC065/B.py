n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
count = 0
current = a[0][0]
for i in range(1, n):
    count += 1
    if current == 2:
        break
    else:
        current = a[current-1][0]
        
print(count if current == 2 else -1)