n = int(input())
a = list(map(int, input().split()))
sort = sorted(a)
result_a = 0
result_b = 0

for i in range(0, n):
    if i % 2 == 0:
        result_a += sort[i]
    else:
        result_b += sort[i]

print(abs(result_a - result_b))