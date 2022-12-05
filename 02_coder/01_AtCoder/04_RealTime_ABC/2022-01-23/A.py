s = list(input())
s2 = []
a, b = map(int, input().split())

for i in range(1, len(s)+1):
    if i == a:
        s2.append(s[b-1])
    elif i == b:
        s2.append(s[a-1])
    else:
        s2.append(s[i-1])
        
print("".join(s2))