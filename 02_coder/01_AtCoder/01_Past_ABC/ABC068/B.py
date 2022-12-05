n = int(input())
l = [1, 2, 4, 8, 16, 32, 64]

# ｎから0まで-1ずつ減少していく → 例100 99 98 97 ...
for i in range(n, 0, -1):
    if i in l:
        print(i)
        break

