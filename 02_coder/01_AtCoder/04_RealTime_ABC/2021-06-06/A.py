x, y = map(int, input().split())

if x - y == 0:
    print(x)
elif 3 - (x + y) < 0:
    print(2)
else:
    print(3 - (x + y))