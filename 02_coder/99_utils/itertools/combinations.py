# ----------------------------------------------------
# combinations -> 文字列の組み合わせを数える
# 組み合わせ・重複なし
# ----------------------------------------------------
# itertoolsのcombinationsメソッドをインポートする
from itertools import combinations

n = int(input(  ))
# 順列（組み合わせ）を求めたいものをリストで用意する
d = list(map(int, input().split()))
result = 0

# リスト(d)の中から2つ（1, 2）のような組み合わせを重複なしで取得
# combinations(d, 3)にすると(1, 2, 3)のように3つになる
x = combinations(d, 2)

# combinationsオブジェクトを全てループで回して足し合わせていく
for i in x:
    result += i[0] * i[1]
    
print(result)