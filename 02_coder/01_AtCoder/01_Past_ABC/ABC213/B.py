n = int(input())
a = [int(i) for i in input().split()]

A = [(a, i+1) for i, a in enumerate(a)]
A.sort()
print(A[-2][1])