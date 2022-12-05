import math
a, b = map(str, input().split())

for i in range(1, 1000):
    if i == math.sqrt(int(a+b)):
        print("Yes")
        exit()

print("No")
