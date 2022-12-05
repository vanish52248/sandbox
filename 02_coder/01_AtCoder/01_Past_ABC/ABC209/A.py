a, b = map(int, input().split())
count = 0

if a <= b:
    for _ in range(a, b + 1):
        count += 1
elif a >= b:
    count = 0
print(count)