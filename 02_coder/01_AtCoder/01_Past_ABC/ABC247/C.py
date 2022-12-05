n = int(input())

current = 1
if n == 1:
    ans = current
else:
    for i in range(2, n+1):
        ans = f"{current} {i} {current}"
        current = ans

print(ans)