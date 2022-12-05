n = int(input())
a = list(set(sorted(list(map(int, input().split())))))
# n = 5 , a = [0, 1, 2, 3, 4]  = 5 のようなケースを想定する
ans = max(a)+1

for i in range(len(a)):
    if i != a[i]:
        ans = i
        break
print(ans)