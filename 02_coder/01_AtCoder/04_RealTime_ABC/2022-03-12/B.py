n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c_all = 0
c_part = 0
temp = []

for i, v in zip(a, b):
    if i == v:
        c_all += 1
        temp.append(i)
print(c_all)

for i in temp:
    if i in a:
        a.remove(i)
for i in temp:
    if i in b:
        b.remove(i)

for i in a:
    if i in b:
        c_part += 1

print(c_part)