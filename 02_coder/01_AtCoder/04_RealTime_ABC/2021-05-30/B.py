n, k = map(int, input().split())
count = 0

for i in range(1, n + 1) : # 1, 2, 3
    for j in range(1, k + 1) : # 1, 2, 3
        count += int(str(i) + "0" + str(j))
print(count)