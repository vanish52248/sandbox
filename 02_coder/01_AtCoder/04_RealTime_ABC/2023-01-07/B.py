t = int(input())

for i in range(t):
    n = int(input())
    test = list(map(int, input().split()))
    count = 0
    for i in test:
        if i % 2 == 1:
            count += 1
    print(count)
