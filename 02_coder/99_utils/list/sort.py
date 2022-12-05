n = int(input())
lst = [list(map(str,input().split())) for _ in range(n)]
# [0, 1]のキーが2つ目の”1”のほうで降順ソート
point_sort = sorted(lst, reverse=True, key=lambda x: x[1])
print(point_sort)


