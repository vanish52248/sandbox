a, b, k = map(int, input().split())

if k >= a + b:
    print(0, 0)
    exit()
else:
    if k >= a:
        k -= a
        a = 0
        if k >= b:
            k -= b
            b = 0
        elif k < b:
            b -= k
    elif k < a:
        a -= k

print(a, b)