# ----------------------------------------------------
# n = カードの枚数(9) m = カードのセット数
# mに３が指定された場合、[1,2,3,4,5,6,7,8,9] → [[1,2,3], [4,5,6], [7,8,9]]になる
# ----------------------------------------------------
from itertools import zip_longest

n, m = list(map(int, input().split()))

card_lst = []
for i in zip_longest(*[iter(range(1, n+1))]*m):
    card_lst.append(list(i))

print(card_lst)