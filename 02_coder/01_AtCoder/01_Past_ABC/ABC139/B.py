a, b = map(int, input().split())

if b == 1 and a > b:
    print(0)
else:
    for i in range(1, 21):
        temp = i * (a-1) +1
        if temp >= b:
            print(i)
            break