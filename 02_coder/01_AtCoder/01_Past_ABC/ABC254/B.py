n = int(input())

lst = []
for i in range(1, n+1):
    temp = [0]*i
    lst.append(temp)

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if j == 0 or j == i:
            lst[i][j] = 1
        else:
            lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

for i in lst:
    print(*i)
