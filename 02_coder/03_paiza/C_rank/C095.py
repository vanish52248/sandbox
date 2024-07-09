n, k = map(int, input().split())

t = sorted([int(input()) for _ in range(n)])

min_lst = {}
for i in t:
    min_lst[i] = abs(k-i)
    
for k, v in min_lst.items():
    if min(min_lst.values()) == v:
        print(k)
        