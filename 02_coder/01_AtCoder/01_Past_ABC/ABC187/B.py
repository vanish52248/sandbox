n = int(input())
count = 0
x_lst = []
y_lst = []

for i in range(n):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

for i in range(n-1):
    for j in range(i+1, n):
        if -1 <= (y_lst[i]-y_lst[j])/(x_lst[i]-x_lst[j]) and (y_lst[i]-y_lst[j])/(x_lst[i]-x_lst[j]) <= 1:
            count += 1
 
print(count)