a, b, c = map(int, input().split())

if c == 0:
    while True:
        a -= 1
        if a <= 0:
            print("Aoki")
            break
        b -= 1
        if b <= 0:
            print("Takahashi")
            break
else:
    while True:
        b -= 1
        if b <= 0:
            print("Takahashi")
            break
        a -= 1
        if a <= 0:
            print("Aoki")
            break
