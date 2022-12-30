a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lst = [a, b, c, d, e]
ans = 0

temp = 10000
other_lst = []
nine_flg = True

min_ = 10000
for i, v in enumerate(lst):
    if str(v)[-1] == "0":
        ans += v
        nine_flg = False
    elif str(v)[-1] == "9":
        ans += v + (10-int(str(v)[-1]))
    else:
        nine_flg = False
        other_lst.append(v)
        if temp > int(str(v)[-1]):
            temp = int(str(v)[-1])
            min_ = v

if len(other_lst) > 0:
    other_lst.remove(min_)

for i in other_lst:
    ans += i + (10-int(str(i)[-1]))

if len(other_lst) > 0:
    print(ans + min_)
elif nine_flg:
    print(ans - 1)
else:
    print(ans)
