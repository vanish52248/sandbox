s = input()
ans = "0"

for i in range(len(s)-1):
    if s[i] == "0":
        ans += "0"
    elif s[i] == "1":
        ans += "1"
print(ans)