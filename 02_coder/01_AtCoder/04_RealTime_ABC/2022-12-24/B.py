n = int(input())
a = list(map(int, input().split()))
q = int(input())

for i in range(q):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        a[lst[1]-1] = lst[2]
    if lst[0] == 2:
        print(a[lst[1]-1])
