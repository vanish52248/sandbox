n = int(input())
s = []
for i in range(n):
    s.append(int(input()))

s_lst = []
for i in s:
    if i % 10 != 0:
        s_lst.append(i)
s_min = min(s_lst) if s_lst else 0

if sum(s) % 10 != 0:
    print(sum(s))
else:
    print(sum(s)-s_min if s_min != 0 else 0)