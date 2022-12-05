n = int(input())
x = list(map(int, input().split()))

p = 100000000
for i in range(100):    
    temp = 0
    for j in x:
        temp += (i - j)**2
    p = min(p, temp)
    
print(p)