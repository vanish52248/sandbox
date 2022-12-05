x, a, b = map(int, input().split())
r = (0 - a) + b
if r > 0:
    if r > x:
        print("dangerous")
    else:
        print("safe")
else:
    print("delicious")