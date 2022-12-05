def base_ten(num):
    num = str(num)
    if "7" in num:
        return True
    else:
        return False

def base_eight(num):
    s = ""
    while num > 0:
        s = str(num%8) + s
        num //= 8
    if "7" in s:
        return True
    else:
        return False
    
n = int(input())
ans = 0
for i in range(1, n+1):
    if not base_ten(i) and not base_eight(i):
        ans += 1

print(ans)