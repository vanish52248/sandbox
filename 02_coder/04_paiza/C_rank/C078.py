n, c1, c2 = map(int, input().split())

p = [int(input()) for _ in range(n)]

amount = 0
kabu = 0
for i in range(len(p)):
    if i+1 == n:
        amount += p[i] * kabu
        kabu = 0
        break
    if p[i] <= c1:
        amount -= p[i]
        kabu += 1
    elif p[i] >= c2:
        amount += p[i] * kabu
        kabu = 0
    elif c1 < p[i] < c2:
        continue
print(amount)
