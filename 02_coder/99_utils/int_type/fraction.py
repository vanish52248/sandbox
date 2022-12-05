# ABC138_B
# ----------------------------------------------------
# 分数の計算　ライブラリ使用
# ----------------------------------------------------

from fractions import Fraction

n = int(input())

a = list(map(int, input().split()))

calc = 0
for i in a:
    # 10, 30 と受け取ってるなら 1/10, 1/30 を約分しながら足し算してくれる
    calc += Fraction(1, i)

# 分母 / 分子を行う
print(calc.denominator / calc.numerator)
    
# ABC138_B
# ----------------------------------------------------
# 分数の計算　ライブラリ不使用
# ----------------------------------------------------

N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in A:
# 10, 30 と受け取ってるなら 1/10, 1/30 を足していく
  ans += 1 / i

print(1 / ans)
