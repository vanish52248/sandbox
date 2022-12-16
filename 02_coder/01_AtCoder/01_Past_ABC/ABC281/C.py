n, t = map(int, input().split())
a = list(map(int, input().split()))

total = sum(a)

temp = t % total

while True:
    for i, v in enumerate(a, start=1):
        if temp - v < 0:
            print(i, temp)
            exit()
        temp -= v
