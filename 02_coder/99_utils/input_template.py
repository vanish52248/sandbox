"""
AtCoder用標準入力テンプレート
コメント部分が受け取る入力内容
 → が出力結果内容
"""

# helloworld
s = input()

# 1
n = int(input())

# hello world
s, t = map(str, input().split())

# 1 2
n, m = map(int, input().split())

# hello world → [hello, world]
lst = list(map(str, input().split()))

# hello world → [hello, world]
lst = [i for i in input().split()]

# set内包表記 a, !a, b, !c, d, !d → {'a', '!c', '!d', 'd', '!a', 'b'}
s = set(input() for i in range(n))

# 1 2 3 4 5  → 1 2 3 4 5
n = map(int, input().split())
for i in n:
    print(i)

# 1 2 3 4 5 → [1, 2, 3, 4, 5]
lst = list(map(int, input()))

# 1 2 3 4 5 → [1, 2, 3, 4, 5]
lst = [int(i) for i in input().split()]

# hello → [h, e, l, l, o]
lst = list(input())

# hello → [h, e, l, l, o]
lst = [i for i in input()]

# 2次元配列の格納 ..##..## → [[., ., #, #, ., ., #, #]]
N=int(input())
S=[list(input()) for _ in range(N)]

# 2次元配列の格納 2 3 4 と 2 3 4で2行(h=2) → [[2, 3, 4], [2, 3, 4]]
h = int(input())
a = []
for i in range(h):
    a.append(list(map(int, input().split())))

# 1234567890 → 90
a = input()[-2:]

# 1234567890 → 123456789
a = input()[:-1]

# ソート格納 1 3 5 2 4 6 → [1, 2, 3, 4, 5, 6]
A = sorted(list(map(int, input().split())))

# 重複なし格納 tokyo akiba ueno → 'akiba', 'tokyo', 'ueno'
t = set(input().split())

# ★ 1 2 3の場合a(index番号)とi(要素) の順でそれぞれ一気に取り出せる
# a→[1, 2, 3]
# A→[0, 1]
# A→[1, 2]
# A→[2, 3] 
a = [int(i) for i in input().split()]
A = [(a, i+1) for i, a in enumerate(a)]
# 一番最後のindexのindex番号を取り出すという出力方法
print(A[-1][1])

# 3 ←ここで個数入力して↓でその個数分標準入力
# 100 ← 一つではなく複数(100, 200, 300 なども受け取れる)
# 200
# 300 → [100, 200, 300]
n = int(input())
a = [input() for _ in range(n)]

# 3 ←ここで個数入力して↓でその個数分標準入力
# 100 200
# 300 400
# 500 600 
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    
# 4 ←ここで個数入力して↓でその個数分標準入力
# 2 1 2 ←一番左の個数分標準入力
# 2 1 1
# 1 1
# 3 1 2 3
n = int(input())
a = [input() for _ in range(n)]
# ↓ 上記のうち重複してない個数をsetに格納してカウント
n = int(input())
l = set(input() for i in range(n))
print(len(l))
