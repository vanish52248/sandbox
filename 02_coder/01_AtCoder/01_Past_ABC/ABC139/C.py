n = int(input())
h = list(map(int, input().split()))
count = 0

for i in range(n-1):
    temp_count = 0
    for j in range(i+1, n):
        if h[i] >= h[j]:
            temp_count += 1
        else:
            break
    count = max(count, temp_count)
    
print(count)