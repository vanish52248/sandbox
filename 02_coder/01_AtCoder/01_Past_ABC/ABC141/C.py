n, k, q = map(int, input().split())
culc_lst = [k] * n

for _ in range(q):
    a = int(input())
    culc_lst = list(map(lambda x: x-1, culc_lst))
    culc_lst[a-1] += 1

for i in culc_lst:
    print("Yes" if i > 0 else "No")