# ABC180_B
# ----------------------------------------------------
# マンハッタン・ユークリッド・チェビシェフ距離
# ----------------------------------------------------
import math

n = int(input())
x = list(map(int, input().split()))

# マンハッタン距離
manhattan = 0
for i in x:
    manhattan += abs(i)

# ユークリッド距離
euclid = 0
for i in x:
    euclid += abs(i**2)
euclid = math.sqrt(euclid)

# チェビシェフ距離
chebyshev = 0
for i in x:
    chebyshev = max(chebyshev, abs(i))

print(manhattan)
print(euclid)
print(chebyshev)
