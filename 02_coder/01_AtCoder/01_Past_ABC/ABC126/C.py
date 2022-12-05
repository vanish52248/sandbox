n, k = map(int, input().split())
point_lst = [i for i in range(1, n+1)]
max_tmp_parent = 0
child = 0

for current_point in point_lst:
    count = 0
    parent = n
    while 1 <= current_point <= k-1:
        current_point *= 2
        count += 1
    parent *= pow(2, count)
    max_tmp_parent = max(max_tmp_parent, parent)
    child += max_tmp_parent // parent
    
print(child / max_tmp_parent)