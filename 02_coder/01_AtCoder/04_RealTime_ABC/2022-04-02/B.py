from math import sqrt
A,B = map(int,input().split())
d = sqrt(A**2 + B**2)
print(d)
print(A / d, B / d)