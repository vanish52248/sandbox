# ----------------------------------------------------
# permutations -> 文字列の組み合わせを数える
# 組み合わせ・重複あり
# ----------------------------------------------------
# itertoolsのpermutationsメソッドをインポートする
from itertools import permutations
# 任意の文字数の文字列をリスト型で1文字ずつ格納 aba → [a, b, a]
s = list(input())
# 空のset変数を作成
st = set()
# permutationsで標準入力の文字列リストを回してset変数に格納していく
# この際、重複無で文字数分の順列を作成してくれる（abaなら3文字分の組み合わせ）
for i in permutations(s):
    st.add(i)

print(st)
# 出力結果→{('a', 'a', 'b'), ('b', 'a', 'a'), ('a', 'b', 'a')}  len(st)で個数カウント
