a = input()
b = input()
c = input()
d = input()
e = input()
temp = [a, b, c, d, e]

zero_lst = []
other_lst = []

for i in temp:
    if i[-1] == "0":
        zero_lst.append(int(i))
    else:
        other_lst.append(int(i))

other_dct = {}
for i in other_lst:
    other_dct[i] = int(i)%10

print(other_dct)

other_sort_dct = dict(sorted(other_dct.items(), key=lambda x:x[1], reverse=True))

ans = sum(zero_lst)
for i, v in enumerate(other_sort_dct.keys()):
    if i == len(other_lst)-1:
        ans += v
    else:
        ans += v + abs(int(str(v)[-1])%10-10)
print(ans)
