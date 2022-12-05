n = int(input())
lst = [2, 1]
temp = 0
for i in range(86):
    temp = lst[i] + lst[i+1]
    lst.append(temp)
    if i == n:
        break
    
print(lst[n])