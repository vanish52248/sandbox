n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
temp = 0

for i in range(n):
    temp += a[i] * b[i] 

print("Yes" if temp == 0 else "No")
