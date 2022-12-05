n, m = map(int, input().split())
lst = [list(map(str, input().split())) for _ in range(m)]

points = []
ac_count = 0
wa_count = 0
for i in range(m):
    if lst[i][0] not in points and lst[i][1] == "AC":
        points.append(lst[i][0])
        ac_count += 1
    elif lst[i][0] not in points and lst[i][1] == "WA":
        wa_count += 1
    
    
print(ac_count, wa_count)    
