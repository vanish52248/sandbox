n = int(input())
s = list(input())
r = ["0"]

for i in range(1, len(s)+1):
    if s[i-1] == "R":
        r.insert(i, str(i))
    elif s[i-1] == "L":
        r.insert(i-1, str(i))

print(r)