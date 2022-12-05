h, w = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(h)]

result = []
for i in range(len(lst[0])):
    tmp = []
    for j in lst:
        tmp.append(j[i])
    result.append(tmp)
    
for i in result:
    print(*i)