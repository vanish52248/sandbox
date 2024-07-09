# ポイントカードの計算
import math

n = int(input())

point = 0
for i in range(n):
    d, p = map(int, input().split())
    # 3のつく日(d)はｐ(購入金額)の３％ポイントつく
    if d == 3 or d == 13 or d == 23 or d == 30 or d == 31:
        point += (math.floor(1.03 * p) - p)
    # 5のつく日(d)はｐ(購入金額)の5％ポイントつく
    elif d == 5 or d == 15 or d == 25:
        point += (math.floor(1.05 * p) - p)
    # 通常時は1%ポイントつく
    else:
        point += math.floor(1.00 * p) // 100

print(point)
