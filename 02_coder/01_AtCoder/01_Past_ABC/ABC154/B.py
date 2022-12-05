s = list(input())
r = ""

for i in s:
    r += i.replace(i, "x")
    
print(r)
