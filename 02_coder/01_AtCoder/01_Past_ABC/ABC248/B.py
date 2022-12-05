a, b, k = map(int, input().split())
count = 0

if a >= b:
    print(count)
else:
    while True:
        count += 1
        a *= k
        if a >= b:
            print(count)
            break