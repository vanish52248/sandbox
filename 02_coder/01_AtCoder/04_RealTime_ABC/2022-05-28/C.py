s = list()
q = int(input())
query_list = []

for i in range(q):
    query_list.append(list(map(int, input().split())))

for i in query_list:
    if i[0] == 1:
        s.append(i[1])        
    elif i[0] == 2:
        temp = i[1]
        count = s.count(i[1])
        current = min(i[2], count)
        for i in range(current):
            s.remove(temp)
    elif i[0] == 3:
        print(max(s)-min(s))