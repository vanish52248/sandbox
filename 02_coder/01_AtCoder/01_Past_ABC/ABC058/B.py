O = input()
E = input()

ans = []
for o, e in zip(O, E):
    ans.append(o)
    ans.append(e)

if len(O) > len(E):
    ans.append(O[-1])

print("".join(ans))