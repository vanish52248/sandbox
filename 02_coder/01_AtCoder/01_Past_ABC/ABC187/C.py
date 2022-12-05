n = int(input())
s = set(input() for i in range(n))
for i in s:
    if f"!{i}" in s:
        print(i)
        exit()
print("satisfiable")
