n, m = map(int, input().split())
judge_lst1 = [False] * n
judge_lst2 = [False] * n

lst = []
for i in range(m):
    lst.append(list(map(int, input().split())))

for i in lst:
    for j in range(len(i)):
        temp = i[j]
        if j == 0:
            judge_lst1[temp-1] = True
        elif j == 1:
            judge_lst2[temp-1] = True

print(judge_lst1)
print(judge_lst2)
