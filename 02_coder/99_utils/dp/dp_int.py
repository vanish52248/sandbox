# ABC229_C
n, w = map(int, input().split())
delicious = 0
temp_glam = 0

a_lst = []
b_lst = []

for i in range(n):
    a, b = map(int, input().split())
    a_lst.append(a)
    b_lst.append(b)

# a_lstをキーに、b_lstを値としてキーのa_lstを降順でソートする(2つのリスト関係は維持したままソート)
# ソート前：a[3, 4, 2], b[1, 2, 3] ソート後： a<キー>】(4, 3, 2), b<値>(2, 1, 3)
a_lst, b_lst = zip(*sorted(zip(a_lst, b_lst), reverse=True))
print(a_lst)
print(b_lst)

# b_lstをキーに、a_lstを値としてキーのb_lstを降順でソートする(2つのリスト関係は維持したままソート)
# ソート前：a[3, 4, 2], b[1, 2, 3] ソート後： a<値>(2, 4, 3), b<キー>(3, 2, 1)
a_lst, b_lst = zip(*sorted(zip(a_lst, b_lst), key=lambda x: x[1], reverse=True))
print(a_lst)
print(b_lst)

for i in range(n):
    # temp_glamと重さのb_lstがＷ以下ならTrue
    if w >= (temp_glam + b_lst[i]):
        delicious += (a_lst[i] * b_lst[i])
        temp_glam += b_lst[i]
    # それ以外はおいしさに残っている重さ分の差額を総和してbreak
    else:
        delicious += a_lst[i] * (w-temp_glam)
        break
print(delicious)