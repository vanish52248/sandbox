n = int(input())
dayly_count = 0
ans = 0

for i in range(n + 1):
    dayly_count += 1
    ans += i
    if ans >= n:
        break


print(dayly_count - 1)