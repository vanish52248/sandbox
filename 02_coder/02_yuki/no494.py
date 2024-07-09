r = "yukicoder"
s = list(input())

for i in range(len(s)):
    if s[i] == "?":
        print(r[i])
        break
