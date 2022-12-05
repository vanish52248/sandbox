n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]

dct = {}
for i in range(1, n+1):
    dct[i] = 0


for i in dct.keys():
    count = 0
    for j in range(m):
        for k in range(2):
            if lst[j][k] == i:
                count += 1
    print(count)