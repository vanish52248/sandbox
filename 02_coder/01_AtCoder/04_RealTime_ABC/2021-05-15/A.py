
# 3つの値を list変数の aで受け取る
a = list(map(int, input().split()))

# 受け取った3つの値のリストを昇順でソートする
a = sorted(a)

# 3つの内の中心値を＊２してそれが左と右で足した数値と＝ならTrue
if a[1] * 2 == a[0] + a[2]:
    print('Yes')
else:
    print('No')