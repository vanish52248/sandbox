n, k = map(int, input().split())
p_all = []

for i in range(n):
    p = sum(map(int, input().split()))
    p_all.append(p)
    
p_all_sort = sorted(p_all, reverse=True)

for i in range(n):
    print("Yes" if p_all_sort[k-1] - p_all[i] <= 300 else "No")    
