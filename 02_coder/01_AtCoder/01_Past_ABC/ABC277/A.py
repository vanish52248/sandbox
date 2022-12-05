n, x = map(int, input().split())
p = list(map(int, input().split()))

for i, v in enumerate(p, start=1):
    if v == x:
        print(i)
        exit()
