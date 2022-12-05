n = int(input())
a_list = list(map(int, input().split()))
ans = 0

for i in a_list:
    if i <= 10:
        continue
    elif i > 10:
        ans += (i - 10)

print(ans)