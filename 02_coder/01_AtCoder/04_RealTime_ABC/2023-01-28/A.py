n = int(input())

count = 0
for _ in range(n):
    s = input()
    if s == "For":
        count += 1
        

if count > n // 2:
    print("Yes")
else:
    print("No")
