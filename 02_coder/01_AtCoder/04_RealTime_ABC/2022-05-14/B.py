n, w = map(int, input().split())
a = list(map(int, input().split()))
count = 0

if n >= 1:
    for i in range(n):
        if a[i] <= w:
            count += 1
if n >= 2:
    for i in range(n):
        for j in range(1, i+1):
            if a[i] + a[j] <= w:
                count += 1
if n >= 3:            
    for i in range(n):
        for j in range(1, i+1):
            for k in range(2, j+2):
                if a[i] + a[j] + a[k] <= w:
                    count += 1

print(count)