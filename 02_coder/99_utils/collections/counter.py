# ----------------------------------------------------
# リストの要素ごとに何が何個あるか数え上げる。
# その中の最大個数を出力 collectionse
# ----------------------------------------------------
from collections import Counter

n = int(input())
a = list(map(int, input().split()))

# リストの中で出現回数が最も多いものを出力する処理（辞書型で取得）
#keyのみの取得→ print(Counter(a).most_common()[0][0])
#valuesのみの取得→ print(Counter(a).most_common()[0][1])

from collections import Counter

s = list(input())

print(Counter(s).most_common()[0][0])

# abbc が入力されたらその中で最も多い要素のキーを出力→b
# print(Counter(s).most_common()[0][1])にすると値の2が出力(何回出てきたか)

# 2次元配列で受け取れるところを無理やり1次元配列にして
# 出現の多い順で全てのvaluesを出力
n, m = map(int, input().split())

lst = []
for _ in range(m):
    a, b = map(int, input().split())
    lst.append(a)
    lst.append(b)

count = Counter(lst)
for i in count.values():
    print(i)   