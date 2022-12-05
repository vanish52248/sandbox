n, x= map(int,input().split())
a = list(map(int,input().split()))

for i in range(n):
    if (i+1) % 2 == 0:
        a[i] -= 1

if sum(a) <= x:
    print("Yes")
else:
    print("No")