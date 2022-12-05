n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(n):
    temp = 0
    for j in range(i,n):
        temp += a[j]
        if temp >= 4:
            count += 1
            break
print(count)
         