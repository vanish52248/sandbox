n, w = map(int, input().split())
delicious = 0
temp_glam = 0

a_lst = []
b_lst = []
for i in range(n):
    a, b = map(int, input().split())
    a_lst.append(a)
    b_lst.append(b)

a_lst, b_lst = zip(*sorted(zip(a_lst, b_lst), reverse=True))
print(a_lst)
print(b_lst)

for i in range(n):
    if w >= (temp_glam + b_lst[i]):
        delicious += (a_lst[i] * b_lst[i])
        temp_glam += b_lst[i]
    else:
        delicious += a_lst[i] * (w-temp_glam)
        break
print(delicious)