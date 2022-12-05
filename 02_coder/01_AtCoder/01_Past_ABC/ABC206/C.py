import itertools

n = int(input())
a = list(map(int, input().split()))

for i in itertools.combinations(a, n):
    print(i)