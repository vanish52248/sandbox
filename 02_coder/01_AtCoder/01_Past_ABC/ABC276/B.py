n, m = map(int, input().split())

dct = {}
for i in range(1, n+1):
    dct[i] = []

for i in range(m):
    a, b = map(int, input().split())
    dct[a].append(b)
    dct[b].append(a)
    
for i, v in dct.items():
    print(len(v), *(sorted(v)))
