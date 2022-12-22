n, m = map(int, input().split())
count = 0
lst = [input() for _ in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        temp = 0
        for h in range(m):
            if lst[i][h] == 'o' or lst[j][h] == 'o':
                temp += 1
            else:
                break
        if temp == m:
            count += 1
print(count)
