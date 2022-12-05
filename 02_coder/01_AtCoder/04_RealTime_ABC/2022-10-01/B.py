n, q = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
for i in range(len(lst)):
    del lst[i][0]

for j in range(q):
    s, t = map(int, input().split())
    print(lst[s-1][t-1])
