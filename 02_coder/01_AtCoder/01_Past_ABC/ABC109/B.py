n = int(input())

lst = [input() for _ in range(n)]

lst2 = [lst[0]]

for i in range(1, len(lst)):
    if lst[i-1][-1] == lst[i][0] and lst[i] not in lst2:
        lst2.append(lst[i])
        continue
    else:
        print("No")
        exit()
print("Yes")
        