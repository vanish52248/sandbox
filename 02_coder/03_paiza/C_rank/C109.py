import re
n = int(input())

t_list = []
current_list = []
for i in range(n):
    current = ""
    t = input()
    t_list.append(t)
    for j in t:
        if j.isdigit():
            current += j
    current_list.append(int(current))
current_list.sort()

for i in current_list:
    for j in t_list:
        if j.endswith(str(i)):
            print(j)
            break
