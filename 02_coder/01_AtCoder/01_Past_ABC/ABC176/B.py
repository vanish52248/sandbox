import pdb
pdb.set_trace()

n = list(map(int, input()))
print("Yes" if sum(n) % 9 == 0 else "No")
