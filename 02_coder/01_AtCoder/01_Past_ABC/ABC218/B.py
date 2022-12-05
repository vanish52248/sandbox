a = [chr(i) for i in range(97, 123)]
p = list(map(int, input().split()))
r = ""

for i in p:
    r += a[i-1]
    
print(r)