n, k = map(str, input().split())
f = 0

if k == "0":
    print(n)
    exit()

for i in range(int(k)):
    g1 = sorted(list(n), reverse=True)
    g2 = sorted(list(n))
    f = int(("").join(g1)) - int(("").join(g2))
    n = list(str(f))
    if f <= 0:
        print(f)
        exit()
        
print(f)