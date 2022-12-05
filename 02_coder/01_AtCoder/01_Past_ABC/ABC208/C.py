import sys
# 配列のコピーを行う（参照のコピーはしない）
import copy
n, k = map(int, input().split())
a = list(map(int, input().split()))
copy_a = copy.copy(a)

while(True):
    if k >= n:
        for i in range(len(a)):
            a[i] += 1
        k -= len(a)
    elif k < n:
        for i in range(len(a)):
            a[i] += 1
            k -= 1
            if k == 0:
                break
    if k == 0:
        for i in range(len(a)):
            print(a[i] - copy_a[i])
        sys.exit()    