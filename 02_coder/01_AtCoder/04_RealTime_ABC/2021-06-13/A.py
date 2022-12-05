a, b = map(int, input().split())

if b % 100 == 0:
    print(a * (b // 100))
else:
    print(a * (b / 100))