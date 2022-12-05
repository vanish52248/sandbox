a, b, c = map(int, input().split())
count = 0

if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
    print(0)
elif  a == b == c:
    print(-1)
else:
    new_a, new_b, new_c = 0, 0, 0
    while (new_a % 2 == 0) and (new_b % 2 == 0) and (new_c % 2 == 0):
        new_a = b // 2 + c // 2 
        new_b = a // 2 + c // 2
        new_c = a // 2 + b // 2
        count += 1
        a = new_a
        b = new_b
        c = new_c

    print(count)
