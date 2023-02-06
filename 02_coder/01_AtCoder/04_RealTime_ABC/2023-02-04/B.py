n, k = map(int, input().split())

lst = []
for i in range(n):
    lst.append(input())

lst2 = []
for i in range(k):
    lst2.append(lst[i])

lst2.sort()

for i in lst2:
    print(i)
